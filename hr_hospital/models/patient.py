from datetime import date
from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = 'hr.hospital.person'
    _description = 'Patient'

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Personal Doctor',
    )
    user_id = fields.Many2one(
        comodel_name='res.partner',
        string='User',
        help='Odoo user associated with this patient (for portal access)'
    )
    birthday = fields.Date()
    age = fields.Integer(
        compute='_compute_age',
        store=True,
    )
    passport_id = fields.Char(
        string='Passport',
    )

    visits_ids = fields.One2many(
        comodel_name='hr.hospital.visit',
        inverse_name='patient_id',
        string='Visits'
    )

    diagnosis_ids = fields.One2many(
        comodel_name='hr.hospital.diagnosis',
        inverse_name='visit_id',
        string='Diagnosis History',
        compute='_compute_diagnosis_ids',
        store=False
    )

    contact_person = fields.Char()

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birthday:
                age = today.year - record.birthday.year
                if (
                    (today.month, today.day) <
                    (record.birthday.month, record.birthday.day)
                ):
                    age -= 1
                record.age = age
            else:
                record.age = 0

    def create_visit_action(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Visit',
            'res_model': 'hr.hospital.visit',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_patient_id': self.id,
                'default_doctor_id': (
                    self.doctor_id.id if self.doctor_id else False
                ),
            }
        }

    @api.depends('visits_ids.diagnosis_ids')
    def _compute_diagnosis_ids(self):
        for patient in self:
            diagnosis_set = patient.visits_ids.mapped('diagnosis_ids')
            patient.diagnosis_ids = diagnosis_set
