from odoo import models, fields

class HRHospitalPatient (models.Model):
    _name = 'hr.hospital.patient'
    _description = 'patient'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    description = fields.Text()

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="ID",
    )
    res_partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string="First Name",
    )
    res_partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string="Second Name",
    )