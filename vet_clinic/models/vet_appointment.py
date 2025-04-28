from odoo import models, fields

class VetAppointment(models.Model):
    _name = 'vet.appointment'
    _description = 'Veterinary Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'appointment_date'

    patient_id = fields.Many2one(comodel_name='vet.patient', string='Пациент', required=True, tracking=True)
    doctor_id = fields.Many2one(comodel_name='vet.doctor', string='Ветеринар', required=True, tracking=True)
    appointment_date = fields.Datetime(string='Дата и время приема', required=True, tracking=True)
    reason = fields.Char(string='Причина обращения', tracking=True)
    state = fields.Selection(selection=[
        ('planned', 'Запланировано'),
        ('done', 'Завершено'),
        ('canceled', 'Отменено')
    ], default='planned', string='Статус приема', tracking=True)
    notes = fields.Text(string='Примечания')
