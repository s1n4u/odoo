from odoo import models, fields

class HRHospitalVisit (models.Model):
    _name = 'hr.hospital.visit'
    _description = 'visit'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    description = fields.Text()

    res_partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string="visit",
    )