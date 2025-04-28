from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    pet_ids = fields.One2many(comodel_name='vet.patient', inverse_name='owner_id', string='Питомцы')

class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_vet_medicine = fields.Boolean(string='Ветеринарный медикамент', default=False)
    medicine_form = fields.Selection(selection=[
        ('tablets', 'Таблетки'),
        ('injection', 'Инъекция'),
        ('liquid', 'Жидкость'),
        ('ointment', 'Мазь'),
        ('other', 'Другое')
    ], string='Форма медикамента')