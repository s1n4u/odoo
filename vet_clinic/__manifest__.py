{
    'name': 'Veterinary Clinic',
    'summary': 'Clinic management system for veterinarians',
    'author': 's1n',
    'website': 'https://odoo.school/',
    'category': 'Services',
    'license': 'OPL-1',
    'version': '17.0.2.2.3',

    'depends': [
        'base',
        'mail',
        'product',
        'web',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/vet_report.xml',
        'reports/report_diagnosis.xml',
        'views/vet_patient_views.xml',
        'views/vet_doctor_views.xml',
        'views/vet_appointment_views.xml',
        'views/vet_diagnosis_views.xml',
        'views/vet_medicine_views.xml',
        'views/res_partner_views.xml',
        'wizard/quick_appointment_wizard_views.xml',
        'views/menus.xml',
        'wizard/quick_appointment_wizard_views.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],

    'installable': True,

}
