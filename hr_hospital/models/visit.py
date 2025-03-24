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

    @api.constrains('doctor_id', 'planned_datetime')
    def _check_doctor_double_booking(self):
        for record in self:
            if record.planned_datetime and record.doctor_id:
                end = record.planned_datetime + timedelta(hours=2)

                overlapping = self.search([
                    ('id', '!=', record.id),
                    ('doctor_id', '=', record.doctor_id.id),
                    ('planned_datetime', '<=', end),
                ], limit=1)

                if overlapping:
                    raise ValidationError(_(
                        "This doctor already has an appointment within 2 hours of the selected time."))
