from odoo import models, fields, api

class VetDiagnosis(models.Model):
    _name = 'vet.diagnosis'
    _description = 'Veterinary Diagnosis and Treatment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'diagnosis_date desc'

    patient_id = fields.Many2one(comodel_name='vet.patient', string='Пациент', required=True, tracking=True)
    doctor_id = fields.Many2one(comodel_name='vet.doctor', string='Врач', required=True, tracking=True)
    diagnosis_date = fields.Date(string='Дата', default=fields.Date.today, required=True, tracking=True)
    diagnosis = fields.Text(string='Диагноз', required=True, tracking=True)
    treatment = fields.Text(string='Лечение', tracking=True)
    medicine_ids = fields.Many2many(comodel_name='vet.medicine', string='Медикаменты')
    recommendations = fields.Text(string='Рекомендации')

    @api.model
    def create(self, vals):
        diagnosis = super(VetDiagnosis, self).create(vals)

        partner_ids = []

        if diagnosis.patient_id and diagnosis.patient_id.owner_id:
            partner_ids.append(diagnosis.patient_id.owner_id.id)

        vet_group = self.env.ref('vet_clinic.group_vet_admin',
                                 raise_if_not_found=False)

        if vet_group:
            vet_users = vet_group.users
            vet_partners = vet_users.mapped('partner_id')
            partner_ids += vet_partners.ids

        if partner_ids:
            diagnosis.message_subscribe(partner_ids=partner_ids)

        return diagnosis