from odoo import models, fields


class Person(models.AbstractModel):
    _name = 'hr.hospital.person'
    _description = 'Abstract Person'

    name = fields.Char(
        compute='_compute_name',
    )
    first_name = fields.Char(
        required=True,
    )
    last_name = fields.Char(
        required=True,
    )
    phone = fields.Char()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], )
    image_1920 = fields.Image(string="Photo")

    def _compute_name(self):
        for record in self:
            record.name = f'{record.first_name} {record.last_name}'
