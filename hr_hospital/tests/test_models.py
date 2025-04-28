from datetime import date
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestDoctor(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestDoctor, self).setUp(*args, **kwargs)
        self.doctor_model = self.env['hr.hospital.doctor']

    def test_create_regular_doctor(self):
        """Test creating a regular doctor"""
        doctor = self.doctor_model.create({
            'name': 'Dr. House',
            'is_intern': False,
        })
        self.assertTrue(doctor)
        self.assertEqual(doctor.name, 'Dr. House')
        self.assertFalse(doctor.is_intern)

    def test_create_intern_with_valid_mentor(self):
        """Test creating an intern with a valid mentor"""
        mentor = self.doctor_model.create({
            'name': 'Dr. Strange',
            'is_intern': False,
        })
        intern = self.doctor_model.create({
            'name': 'Intern Smith',
            'is_intern': True,
            'mentor_id': mentor.id,
        })
        self.assertEqual(intern.mentor_id, mentor)
        self.assertTrue(intern.is_intern)

    def test_intern_cannot_be_mentor(self):
        """Test that an intern cannot be assigned as a mentor"""
        intern_mentor = self.doctor_model.create({
            'name': 'Intern Mentor',
            'is_intern': True,
        })
        with self.assertRaises(ValidationError):
            self.doctor_model.create({
                'name': 'Intern with wrong mentor',
                'is_intern': True,
                'mentor_id': intern_mentor.id,
            })

class TestDoctorPatient(TransactionCase):

    def setUp(self):
        super().setUp()

        # Создаем тестовую специальность
        self.specialty = self.env['hr.hospital.specialty'].create({
            'name': 'Cardiology'
        })

        # Создаем тестового доктора-ментора
        self.doctor = self.env['hr.hospital.doctor'].create({
            'name': 'Dr. House',
            'specialty_id': self.specialty.id,
            'is_intern': False,
        })

        # Создаем тестового интерна
        self.intern = self.env['hr.hospital.doctor'].create({
            'name': 'Dr. Student',
            'specialty_id': self.specialty.id,
            'is_intern': True,
            'mentor_id': self.doctor.id,
        })

    def test_create_doctor(self):
        """Проверяем, что доктор успешно создается"""
        doctor = self.env['hr.hospital.doctor'].create({
            'name': 'Dr. Strange',
            'specialty_id': self.specialty.id,
            'is_intern': False,
        })
        self.assertTrue(doctor.id)
        self.assertEqual(doctor.is_intern, False)

    def test_create_intern_with_intern_mentor(self):
        """Проверяем, что интерн не может быть ментором другому интерну"""
        bad_mentor = self.env['hr.hospital.doctor'].create({
            'name': 'Fake Mentor',
            'specialty_id': self.specialty.id,
            'is_intern': True,
        })
        with self.assertRaises(ValidationError):
            self.env['hr.hospital.doctor'].create({
                'name': 'Intern 2',
                'specialty_id': self.specialty.id,
                'is_intern': True,
                'mentor_id': bad_mentor.id,
            })

    def test_create_patient(self):
        """Проверяем, что пациент успешно создается"""
        patient = self.env['hr.hospital.patient'].create({
            'name': 'John Doe',
            'birthday': date(2000, 5, 1),
            'doctor_id': self.doctor.id,
        })
        self.assertTrue(patient.id)
        self.assertEqual(patient.doctor_id, self.doctor)

    def test_patient_age_calculation(self):
        """Проверяем правильность расчета возраста"""
        today = date.today()
        birth_year = today.year - 30
        birthday = date(birth_year, today.month, today.day)
        patient = self.env['hr.hospital.patient'].create({
            'name': 'Age Test',
            'birthday': birthday,
            'doctor_id': self.doctor.id,
        })
        patient._compute_age()
        self.assertEqual(patient.age, 30)