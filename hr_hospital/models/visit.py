from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Visit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Patient Visit'

    status = fields.Selection([
        ('planned', 'Planned'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='planned')

    planned_datetime = fields.Datetime(string='Planned Date')
    actual_datetime = fields.Datetime(string='Actual Visit Date')
    doctor_id = fields.Many2one('hr.hospital.doctor', string='Doctor', required=True)
    patient_id = fields.Many2one('hr.hospital.patient', string='Patient', required=True)
    diagnosis_ids = fields.One2many('hr.hospital.diagnosis', 'visit_id', string='Diagnoses')

    @api.constrains('doctor_id', 'patient_id', 'planned_datetime')
    def _check_unique_visit(self):
        for record in self:
            if record.planned_datetime:
                existing = self.search([
                    ('id', '!=', record.id),
                    ('doctor_id', '=', record.doctor_id.id),
                    ('patient_id', '=', record.patient_id.id),
                    ('planned_datetime', '=', record.planned_datetime.date())
                ])
                if existing:
                    raise ValidationError("Patient already has a visit with this doctor on the same day.")

    def unlink(self):
        for record in self:
            if record.diagnosis_ids:
                raise ValidationError("You cannot delete a visit with diagnoses.")
        return super().unlink()
