from odoo import models, fields, api
from odoo.tools.translate import _

class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _inherit = 'hr.hospital.person'
    _description = 'Doctor'

    specialty_id = fields.Many2one('hr.hospital.specialty', string='Specialty')
    is_intern = fields.Boolean(string='Intern')
    mentor_id = fields.Many2one('hr.hospital.doctor', string='Mentor')

    @api.constrains('mentor_id')
    def _check_mentor_not_intern(self):
        for record in self:
            if record.mentor_id and record.mentor_id.is_intern:
                raise models.ValidationError(_("An intern cannot be a mentor."))
