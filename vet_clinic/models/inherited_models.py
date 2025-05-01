from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    pet_ids = fields.One2many(comodel_name='vet.patient',
                              inverse_name='owner_id', string='Pets')


class VetDisease(models.Model):
    _name = 'vet.disease'
    _description = 'Disease'

    name = fields.Char(required=True)
    description = fields.Text()
