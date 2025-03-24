from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    visit_id = fields.Many2one(
        comodel_name='hr.hospital.visit',
        string='Visit',
        required=True,
    )
    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string='Disease',
        required=True,
    )
    description = fields.Text(
        string='Treatment Description',
    )
    approved = fields.Boolean()

    @api.constrains('approved')
    def _check_mentor_approval(self):
        for record in self:
            doctor = record.visit_id.doctor_id
            if doctor.is_intern and record.approved and not doctor.mentor_id:
                raise ValidationError(_("Intern's diagnosis must be approved by a mentor."))
