from datetime import date
from odoo import models, fields, api

class VetPatient(models.Model):
    _name = 'vet.patient'
    _description = 'Veterinary Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Имя животного', required=True, tracking=True)
    species = fields.Selection(selection=[
        ('dog', 'Собака'),
        ('cat', 'Кошка'),
        ('bird', 'Птица'),
        ('other', 'Другое'),
    ], string='Вид', required=True, tracking=True)
    breed = fields.Char(string='Порода', tracking=True)
    birthday = fields.Date(string='Дата рождения', tracking=True)
    age = fields.Integer(
        compute='_compute_age',
        store=True,
    )
    owner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Владелец',
        required=True,
        tracking=True,
    )
    owner_email = fields.Char(
        comodel_name='res.partner',
        string='Email',
        related='owner_id.email',
        store=True,
        readonly=False,
    )
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], )
    image = fields.Image(string='Фото')
    notes = fields.Text(string='Примечания')

    def open_quick_appointment_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Быстрая запись',
            'res_model': 'quick.appointment.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_patient_id': self.id,
            },
        }

    @api.onchange('owner_email')
    def _onchange_owner_email(self):
        if self.owner_email:
            existing_owner = self.env['res.partner'].search([
                ('email', '=', self.owner_email)
            ], limit=1)
            if existing_owner:
                self.owner_id = existing_owner.id

    @api.model
    def create(self, vals):
        patient = super(VetPatient, self).create(vals)
        partner_ids = []
        if patient.owner_id:
            partner_ids.append(patient.owner_id.id)

        vet_group = self.env.ref('vet_clinic.group_vet_admin', raise_if_not_found=False)

        if vet_group:
            vet_users = vet_group.users
            vet_partners = vet_users.mapped('partner_id')
            partner_ids += vet_partners.ids

        if partner_ids:
            patient.message_subscribe(partner_ids=partner_ids)

        return patient
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
