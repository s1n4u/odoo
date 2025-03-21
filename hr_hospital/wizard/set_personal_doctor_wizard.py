from odoo import models, fields, api

class SetPersonalDoctorWizard(models.TransientModel):
    _name = 'hr.hospital.set.personal.doctor.wizard'
    _description = 'Wizard to set personal doctor for selected patients'

    doctor_id = fields.Many2one('hr.hospital.doctor', string='New Personal Doctor', required=True)

    def action_set_doctor(self):
        active_ids = self.env.context.get('active_ids')
        if active_ids:
            patients = self.env['hr.hospital.patient'].browse(active_ids)
            for patient in patients:
                patient.personal_doctor_id = self.doctor_id.id
