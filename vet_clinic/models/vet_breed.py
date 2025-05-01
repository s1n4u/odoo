from odoo import models, fields

class VetBreed(models.Model):
    _name = 'vet.breed'
    _description = 'Порода животного'

    name = fields.Char(string='Название породы', required=True)
    species_id = fields.Many2one(comodel_name='vet.species', string='Вид', required=True)
