from odoo import models, fields


class VetBreed(models.Model):
    _name = 'vet.breed'
    _description = 'Animal Breed'

    name = fields.Char(string='Breed Name', required=True)
    species_id = fields.Many2one(comodel_name='vet.species', string='Species',
                                 required=True)
