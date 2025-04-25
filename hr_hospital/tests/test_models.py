from odoo.tests.common import TransactionCase
from datetime import date


class TestHrHospital(TransactionCase):
    def setUp(self):
        super().setUp()
        Doctor = self.env['hr.hospital.doctor']
        Patient = self.env['hr.hospital.patient']
        Visit = self.env['hr.hospital.visit']
        self.doctor = Doctor.create({
            'first_name': 'Іван',
            'last_name': 'Іванов',
        })
        self.patient = Patient.create({
            'first_name': 'Петро',
            'last_name': 'Петров',
            'birthday': date(2000, 1, 1),
            'doctor_id': self.doctor.id,
        })
        self.visit = Visit.create({
            'doctor_id': self.doctor.id,
            'patient_id': self.patient.id,
            'planned_datetime': date.today(),
        })

    def test_patient_age_compute(self):
        self.assertEqual(self.patient.age, date.today().year - 2000)

    def test_doctor_cannot_double_book(self):
        Visit = self.env['hr.hospital.visit']
        with self.assertRaises(Exception):
            Visit.create({
                'doctor_id': self.doctor.id,
                'patient_id': self.patient.id,
                'planned_datetime': date.today(),
            })
