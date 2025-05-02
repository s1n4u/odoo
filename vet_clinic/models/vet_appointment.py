from odoo import models, fields, api


class VetAppointment(models.Model):
    _name = 'vet.appointment'
    _description = 'Veterinary Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'appointment_date'

    patient_id = fields.Many2one(comodel_name='vet.patient', string='Patient',
                                 required=True, tracking=True)
    doctor_id = fields.Many2one(comodel_name='vet.doctor',
                                string='Veterinarian', required=True,
                                tracking=True)
    appointment_date = fields.Datetime(string='Appointment Date & Time',
                                       required=True, tracking=True)
    reason = fields.Char(tracking=True)
    state = fields.Selection(selection=[
        ('planned', 'Planned'),
        ('done', 'Completed'),
        ('canceled', 'Canceled')
    ], default='planned', string='Status', tracking=True)
    notes = fields.Text()
