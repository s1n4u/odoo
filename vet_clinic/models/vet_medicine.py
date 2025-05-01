from odoo import models, fields

class VetMedicine(models.Model):
    _name = 'vet.medicine'
    _description = 'Veterinary Medicine'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Название', required=True, tracking=True)
    manufacturer = fields.Char(string='Производитель', tracking=True)
    medicine_form = fields.Selection(selection=[
        ('tablet', 'Таблетки'),
        ('capsule', 'Капсулы'),
        ('liquid', 'Жидкость'),
        ('injection', 'Инъекция'),
        ('ointment', 'Мазь'),
        ('other', 'Другое')
    ], string='Форма выпуска', required=True, tracking=True)
    price = fields.Float(string='Цена', tracking=True)
    expiration_date = fields.Date(string='Срок годности', tracking=True)
    quantity = fields.Integer(string='Количество на складе', tracking=True)
    notes = fields.Text(string='Заметки')
