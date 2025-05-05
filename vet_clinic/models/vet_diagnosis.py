from odoo import models, fields, api


class VetDiagnosis(models.Model):
    _name = 'vet.diagnosis'
    _description = 'Veterinary Diagnosis and Treatment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'diagnosis_date desc'

    patient_id = fields.Many2one(comodel_name='vet.patient', string='Patient',
                                 required=True, tracking=True)
    doctor_id = fields.Many2one(comodel_name='vet.doctor',
                                string='Veterinarian', required=True,
                                tracking=True)
    diagnosis_date = fields.Date(string='Date', default=fields.Date.today,
                                 required=True, tracking=True)
    disease_id = fields.Many2one(comodel_name='vet.disease', string='Disease',
                                 tracking=True)
    treatment = fields.Text(tracking=True)
    medicine_ids = fields.Many2many(comodel_name='vet.medicine',
                                    string='Medications')
    recommendations = fields.Text()

    name = fields.Char(string="Diagnosis ID", required=True, copy=False,
                       readonly=True, default='New')

    def action_print_diagnosis(self):
        return self.env.ref('vet_clinic.vet_diagnosis_report').report_action(
            self)

    class VetDiagnosis(models.Model):
        _name = 'vet.diagnosis'
        _inherit = ['mail.thread', 'mail.activity.mixin']
        _description = 'Veterinary Diagnosis and Treatment'

        @api.model_create_multi
        def create(self, vals_list):
            diagnoses = super().create(vals_list)

            vet_group = self.env.ref('vet_clinic.group_vet_admin',
                                     raise_if_not_found=False)
            vet_partners = vet_group.users.mapped(
                'partner_id') if vet_group else self.env['res.partner']

            for diagnosis in diagnoses:
                partner_ids = []

                if diagnosis.patient_id and diagnosis.patient_id.owner_id:
                    partner_ids.append(diagnosis.patient_id.owner_id.id)

                partner_ids += vet_partners.ids

                if partner_ids:
                    diagnosis.message_subscribe(partner_ids=partner_ids)

            return diagnoses

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'vet.diagnosis') or 'New'
        return super(VetDiagnosis, self).create(vals)
