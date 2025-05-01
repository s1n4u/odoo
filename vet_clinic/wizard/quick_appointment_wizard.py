from odoo import models, fields


class QuickAppointmentWizard(models.TransientModel):
    _name = 'quick.appointment.wizard'
    _description = 'Wizard for Quick Appointment Booking'

    patient_id = fields.Many2one(comodel_name='vet.patient', required=True)
    doctor_id = fields.Many2one(comodel_name='vet.doctor', required=True)
    appointment_date = fields.Datetime(required=True)
    reason = fields.Char()

    def create_appointment(self):
        self.ensure_one()
        self.env['vet.appointment'].create({
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            'appointment_date': self.appointment_date,
            'reason': self.reason,
        })
        return {'type': 'ir.actions.act_window_close'}
