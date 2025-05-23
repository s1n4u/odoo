from odoo import models, fields


class VetMedicine(models.Model):
    _name = 'vet.medicine'
    _description = 'Veterinary Medicine'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    manufacturer = fields.Char(tracking=True)
    medicine_form = fields.Selection(selection=[
        ('tablet', 'Tablet'),
        ('capsule', 'Capsule'),
        ('liquid', 'Liquid'),
        ('injection', 'Injection'),
        ('ointment', 'Ointment'),
        ('other', 'Other')
    ], string='Form', required=True, tracking=True)
    price = fields.Float(tracking=True)
    expiration_date = fields.Date(tracking=True)
    quantity = fields.Integer(string='Stock Quantity', tracking=True)
    notes = fields.Text()
