from odoo import models, fields


class DiagnosisReportWizard(models.TransientModel):
    _name = 'hr.hospital.diagnosis.report.wizard'
    _description = 'Diagnosis Report Wizard'

    doctor_ids = fields.Many2many(comodel_name='hr.hospital.doctor',
                                  string='Doctors')
    disease_ids = fields.Many2many(comodel_name='hr.hospital.disease',
                                   string='Diseases')
    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')

    def action_show_report(self):
        domain = []

        if self.doctor_ids:
            domain.append(('visit_id.doctor_id', 'in', self.doctor_ids.ids))

        if self.disease_ids:
            domain.append(('disease_id', 'in', self.disease_ids.ids))

        if self.date_from:
            domain.append(('create_date', '>=', self.date_from))

        if self.date_to:
            domain.append(('create_date', '<=', self.date_to))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Diagnosis Report',
            'res_model': 'hr.hospital.diagnosis',
            'view_mode': 'tree,form',
            'domain': domain,
            'target': 'current',
        }
