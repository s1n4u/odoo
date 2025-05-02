from odoo.tests.common import TransactionCase
from datetime import date


class TestVetMedicine(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Medicine = self.env['vet.medicine']

    def test_create_medicine_valid(self):
        """Test creating a valid veterinary medicine."""
        medicine = self.Medicine.create({
            'name': 'Amoxicillin',
            'manufacturer': 'VetPharma',
            'medicine_form': 'tablet',
            'price': 24.99,
            'expiration_date': date(2025, 12, 31),
            'quantity': 100,
            'notes': 'For infections.'
        })

        self.assertTrue(medicine)
        self.assertEqual(medicine.name, 'Amoxicillin')
        self.assertEqual(medicine.medicine_form, 'tablet')
        self.assertEqual(medicine.quantity, 100)

    def test_required_fields(self):
        """Test that required fields (name, medicine_form) are enforced."""
        with self.assertRaises(Exception):
            self.Medicine.create({
                'medicine_form': 'capsule'  # no name
            })

        with self.assertRaises(Exception):
            self.Medicine.create({
                'name': 'Baytril'  # no medicine_form
            })

    def test_field_types(self):
        """Test optional fields and data types."""
        medicine = self.Medicine.create({
            'name': 'Metacam',
            'medicine_form': 'liquid',
            'price': 12.5,
            'quantity': 30,
        })
        self.assertIsInstance(medicine.price, float)
        self.assertIsInstance(medicine.quantity, int)
        self.assertFalse(medicine.expiration_date)  # Field left blank
