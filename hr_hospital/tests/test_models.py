from datetime import date
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestDoctor(TransactionCase):

    def setUp(self):
        super().setUp()
        self.doctor_model = self.env['hr.hospital.doctor']
        self.specialty_model = self.env['hr.hospital.specialty']

        self.specialty = self.specialty_model.create({
            'name': 'Cardiology',
        })

    def test_create_regular_doctor(self):
        doctor = self.doctor_model.create({
            'first_name': 'Gregory',
            'last_name': 'House',
            'specialty_id': self.specialty.id,
            'is_intern': False,
        })
        self.assertTrue(doctor.id)
        self.assertEqual(doctor.is_intern, False)

    def test_create_intern_with_valid_mentor(self):
        mentor = self.doctor_model.create({
            'first_name': 'Meredith',
            'last_name': 'Grey',
            'specialty_id': self.specialty.id,
            'is_intern': False,
        })
        intern = self.doctor_model.create({
            'first_name': 'Alex',
            'last_name': 'Karev',
            'specialty_id': self.specialty.id,
            'is_intern': True,
            'mentor_id': mentor.id,
        })
        self.assertEqual(intern.mentor_id, mentor)

    def test_intern_cannot_be_mentor(self):
        intern_mentor = self.doctor_model.create({
            'first_name': 'George',
            'last_name': 'O\'Malley',
            'specialty_id': self.specialty.id,
            'is_intern': True,
        })
        with self.assertRaises(ValidationError):
            self.doctor_model.create({
                'first_name': 'Cristina',
                'last_name': 'Yang',
                'specialty_id': self.specialty.id,
                'is_intern': True,
                'mentor_id': intern_mentor.id,
            })


class TestDoctorPatient(TransactionCase):

    def setUp(self):
        super().setUp()
        self.specialty_model = self.env['hr.hospital.specialty']
        self.doctor_model = self.env['hr.hospital.doctor']
        self.patient_model = self.env['hr.hospital.patient']

        self.specialty = self.specialty_model.create({
            'name': 'General Medicine',
        })

        self.doctor = self.doctor_model.create({
            'first_name': 'John',
            'last_name': 'Dorian',
            'specialty_id': self.specialty.id,
            'is_intern': False,
        })

    def test_create_doctor(self):
        doctor = self.doctor_model.create({
            'first_name': 'Elliot',
            'last_name': 'Reid',
            'specialty_id': self.specialty.id,
            'is_intern': False,
        })
        self.assertTrue(doctor.id)

    def test_create_patient(self):
        patient = self.patient_model.create({
            'first_name': 'Carla',
            'last_name': 'Espinosa',
            'doctor_id': self.doctor.id,
            'birthday': date(1990, 5, 5),
        })
        self.assertTrue(patient.id)
        self.assertEqual(patient.doctor_id, self.doctor)

    def test_patient_age_calculation(self):
        today = date.today()
        birth_year = today.year - 25
        birthday = date(birth_year, today.month, today.day)
        patient = self.patient_model.create({
            'first_name': 'Turk',
            'last_name': 'Todd',
            'doctor_id': self.doctor.id,
            'birthday': birthday,
        })
        patient._compute_age()
        self.assertEqual(patient.age, 25)
