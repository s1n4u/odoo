from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    hr_hospital_doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor',
        string='Doctors',
    )

    hr_hospital_patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient',
        string='Patient',
    )

    hr_hospital_disease_ids = fields.Many2many(
        comodel_name='hr.hospital.disease',
        string='Disease',
    )

    hr_hospital_visit_ids = fields.Many2many(
        comodel_name='hr.hospital.visit',
        string='Visit',
    )