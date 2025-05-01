from odoo import models, fields

class VetSpecies(models.Model):
    _name = 'vet.species'
    _description = 'Вид животного'

    name = fields.Char(string='Название', required=True)
    breed_ids = fields.One2many(comodel_name='vet.breed', inverse_name='species_id', string='Породы')