from odoo import models, fields, api
from odoo.tools.translate import _


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _inherit = 'hr.hospital.person'

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=False,
        tracking=True,
    )
    _description = 'Doctor'

    specialty_id = fields.Many2one(
        comodel_name='hr.hospital.specialty',
        string='Specialty',
    )
    is_intern = fields.Boolean(
        string='Intern',
    )
    mentor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Mentor',
        domain=[('is_intern', '=', False)],
    )

    intern_ids = fields.One2many(
        comodel_name='hr.hospital.doctor',
        inverse_name='mentor_id',
        string='Interns',
    )

    visit_ids = fields.One2many(
        comodel_name='hr.hospital.visit',
        inverse_name='doctor_id',
        string='Visits',
    )

    company_id = fields.Many2one(
        comodel_name='res.company',
        string="Company",
        default=lambda self: self.env.company,
        readonly=True
    )

    @api.constrains('mentor_id')
    def _check_mentor_not_intern(self):
        for record in self:
            if record.mentor_id and record.mentor_id.is_intern:
                raise models.ValidationError(
                    _("An intern cannot be a mentor."))
