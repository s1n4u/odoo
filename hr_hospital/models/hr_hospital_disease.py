from odoo import models,fields

class HRHospitalDisease (models.Model):
    _name = 'hr.hospital.disease'
    _description = 'disease'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    description = fields.Text()

    res_partner_ids = fields.Many2one(
        comodel_name='res.partner',
        string="Disease",
    )