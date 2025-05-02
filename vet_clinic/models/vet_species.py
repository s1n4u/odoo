from odoo import models, fields


class VetSpecies(models.Model):
    _name = 'vet.species'
    _description = 'Animal Species'

    name = fields.Char(required=True)
    breed_ids = fields.One2many(comodel_name='vet.breed',
                                inverse_name='species_id',
                                string='Breeds',
                                )
