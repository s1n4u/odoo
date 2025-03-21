from odoo import models, fields, api
from datetime import date

class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = 'hr.hospital.person'
    _description = 'Patient'

    doctor_id = fields.Many2one('hr.hospital.doctor', string='Personal Doctor')
    birthday = fields.Date(string='Birthday')
    age = fields.Integer(compute='_compute_age', store=True)
    passport_id = fields.Char(string='Passport')
    contact_person = fields.Char(string='Contact Person')

    personal_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Personal Doctor'
    )

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birthday:
                age = today.year - record.birthday.year
                if (today.month, today.day) < (record.birthday.month, record.birthday.day):
                    age -= 1
                record.age = age
            else:
                record.age = 0
