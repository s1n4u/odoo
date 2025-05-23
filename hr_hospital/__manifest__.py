{
    'name': 'Hospital Management Extended',
    'summary': 'Hospital module with diagnoses and patient wizards',
    'author': 's1n',
    'website': 'https://odoo.school/',
    'category': 'Healthcare',
    'license': 'OPL-1',
    'version': '17.0.2.2.0',
    'depends': ['base'],
    'data': [
        'security/hr_hospital_groups.xml',
        'security/ir.model.access.csv',
        'security/visit_rule.xml',
        'security/patient_rule.xml',
        'views/doctor_report.xml',
        'wizard/diagnosis_report_wizard_view.xml',

        'data/disease_demo.xml',
        'data/demo_specialties.xml',
        'data/demo_users.xml',
        'data/demo_persons.xml',
        'data/visit_demo.xml',

        'views/person_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
        'views/menu.xml',
        'views/specialty_views.xml',


        'wizard/set_personal_doctor_wizard_view.xml',



    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],

    'i18n': True,
}
