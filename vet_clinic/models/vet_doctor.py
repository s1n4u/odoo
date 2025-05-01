from odoo import models, fields


class VetDoctor(models.Model):
    _name = 'vet.doctor'
    _description = 'Veterinary Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=False,
        tracking=False,
    )

    name = fields.Char(
        string='Name',
        related='user_id.name',
        store=True,
        readonly=False,
    )
    phone = fields.Char(
        string='Phone',
        related='user_id.partner_id.phone',
        store=True,
        readonly=False,
    )
    email = fields.Char(
        string='Email',
        related='user_id.partner_id.email',
        store=True,
        readonly=False,
    )
    experience_years = fields.Integer(string='Years of Experience',
                                      tracking=True)
    notes = fields.Text(string='Notes')
