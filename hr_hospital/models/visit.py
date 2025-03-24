from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class Visit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Patient Visit'

    status = fields.Selection([
        ('planned', 'Planned'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ],
        default='planned',
    )

    actual_datetime = fields.Datetime(
        string='Actual Date',
        default=lambda self: fields.Datetime.now()
    )
    planned_datetime = fields.Datetime(
        string='Planned Visit Date',
    )
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor', required=True,
    )
    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
        required=True,
    )
    diagnosis_ids = fields.One2many(
        comodel_name='hr.hospital.diagnosis',
        inverse_name='visit_id',
        string='Diagnoses',
    )

    @api.constrains('doctor_id', 'patient_id', 'planned_datetime')
    def _check_unique_visit(self):
        for record in self:
            if record.planned_datetime:
                visit_day = record.planned_datetime.date()
                start_of_day = fields.Datetime.from_string(f"{visit_day} 00:00:00")
                end_of_day = fields.Datetime.from_string(f"{visit_day} 23:59:59")

                existing = self.search([
                    ('id', '!=', record.id),
                    ('doctor_id', '=', record.doctor_id.id),
                    ('patient_id', '=', record.patient_id.id),
                    ('planned_datetime', '>=', start_of_day),
                    ('planned_datetime', '<=', end_of_day),
                ], limit=1)

                if existing:
                    raise ValidationError(_(
                        "This patient already has a visit with this doctor on the same day."))

    @api.constrains('doctor_id', 'planned_datetime')
    def _check_doctor_double_booking(self):
        for record in self:
            if record.planned_datetime and record.doctor_id:
                end_window = record.planned_datetime + timedelta(hours=2)

                overlapping = self.search([
                    ('id', '!=', record.id),
                    ('doctor_id', '=', record.doctor_id.id),
                    ('planned_datetime', '>=', record.planned_datetime),
                    ('planned_datetime', '<', end_window),
                ], limit=1)

                if overlapping:
                    raise ValidationError(_(
                        "This doctor already has another appointment within 2 hours of the selected time."))

    def unlink(self):
        for record in self:
            if record.diagnosis_ids:
                raise ValidationError(_(
                    "You cannot delete a visit with diagnoses."))
        return super().unlink()