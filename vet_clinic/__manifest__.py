{
    'name': 'Veterinary Clinic',
    'version': '1.0',
    'summary': 'Clinic management system for veterinarians',
    'category': 'Services',
    'author': 's1n',
    'depends': ['base', 'mail', 'product'],
    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',
        'views/vet_patient_views.xml',
        'views/vet_doctor_views.xml',
        'views/vet_appointment_views.xml',
        'views/vet_diagnosis_views.xml',
        'views/vet_medicine_views.xml',
        'views/res_partner_views.xml',
#        'wizard/quick_appointment_wizard_views.xml',
        'reports/vet_report.xml',
        'views/menus.xml',
    ],
    'demo': ['demo/demo_data.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [],
    },
}
