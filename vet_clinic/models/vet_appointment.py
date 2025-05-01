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
    reason = fields.Char(string='Reason', tracking=True)
    state = fields.Selection(selection=[
        ('planned', 'Planned'),
        ('done', 'Completed'),
        ('canceled', 'Canceled')
    ], default='planned', string='Status', tracking=True)
    notes = fields.Text(string='Notes')

    color = fields.Integer(string='Color', compute='_compute_color',
                           store=True)

    @api.depends('state')
    def _compute_color(self):
        for rec in self:
            if rec.state == 'planned':
                rec.color = 3
            elif rec.state == 'done':
                rec.color = 10
            elif rec.state == 'canceled':
                rec.color = 1
            else:
                rec.color = 0
