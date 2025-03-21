from odoo import models, fields

class Person(models.AbstractModel):
    _name = 'hr.hospital.person'
    _description = 'Abstract Person'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    phone = fields.Char()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], )
    image_1920 = fields.Image(string="Photo")
