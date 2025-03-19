from odoo import models, fields

class VetPatient(models.Model):
    _name = 'vet.patient'
    _description = 'Veterinary Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Имя животного', required=True, tracking=True)
    species = fields.Selection([
        ('dog', 'Собака'),
        ('cat', 'Кошка'),
        ('bird', 'Птица'),
        ('other', 'Другое'),
    ], string='Вид', required=True, tracking=True)
    breed = fields.Char(string='Порода', tracking=True)
    birth_date = fields.Date(string='Дата рождения', tracking=True)
    owner_id = fields.Many2one('res.partner', string='Владелец', required=True, tracking=True)
    image = fields.Image(string='Фото')
    notes = fields.Text(string='Примечания')
