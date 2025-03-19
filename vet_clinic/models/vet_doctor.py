from odoo import models, fields

class VetDoctor(models.Model):
    _name = 'vet.doctor'
    _description = 'Veterinary Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Имя врача', required=True, tracking=True)
    specialization = fields.Char(string='Специализация', tracking=True)
    phone = fields.Char(string='Телефон', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    experience_years = fields.Integer(string='Опыт работы (лет)', tracking=True)
    notes = fields.Text(string='Заметки')
