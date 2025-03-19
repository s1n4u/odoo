from odoo import models, fields

class VetDiagnosis(models.Model):
    _name = 'vet.diagnosis'
    _description = 'Veterinary Diagnosis and Treatment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'diagnosis_date desc'

    patient_id = fields.Many2one('vet.patient', string='Пациент', required=True, tracking=True)
    doctor_id = fields.Many2one('vet.doctor', string='Врач', required=True, tracking=True)
    diagnosis_date = fields.Date(string='Дата', default=fields.Date.today, required=True, tracking=True)
    diagnosis = fields.Text(string='Диагноз', required=True, tracking=True)
    treatment = fields.Text(string='Лечение', tracking=True)
    medicine_ids = fields.Many2many('vet.medicine', string='Медикаменты')
    recommendations = fields.Text(string='Рекомендации')
