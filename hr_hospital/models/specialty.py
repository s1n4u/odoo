from odoo import models, fields


class Specialty(models.Model):
    _name = 'hr.hospital.specialty'
    _description = 'Medical Specialty'

    name = fields.Char(
        required=True,
    )
