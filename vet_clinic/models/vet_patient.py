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
    birth_date = fields.Date(string='Дата рождения', tracking=True)
    owner_id = fields.Many2one(comodel_name='res.partner', string='Владелец', required=True, tracking=True)
    owner_email = fields.Char(
        comodel_name='res.partner',
        string='Email',
        related='owner_id.email',
        store=True,
        readonly=False,
    )
    image = fields.Image(string='Фото')
    notes = fields.Text(string='Примечания')

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

        # Добавляем владельца
        if patient.owner_id:
            partner_ids.append(patient.owner_id.id)

        # Добавляем всех пользователей из группы ветеринаров
        vet_group = self.env.ref('hr_hospital.group_vet_admin', raise_if_not_found=False)  # <-- Укажи тут свой модуль и ID группы

        if vet_group:
            vet_users = vet_group.users  # Это пользователи (res.users)
            vet_partners = vet_users.mapped('partner_id')  # Достаём их партнёров
            partner_ids += vet_partners.ids

        if partner_ids:
            patient.message_subscribe(partner_ids=partner_ids)

        return patient