{

    'name': 'Hospital Management Extended',
    'summary': 'Extended hospital module with diagnoses, hierarchy and wizards',
    'author': 's1n',
    'website': 'https://odoo.school/',
    'category': 'Healthcare',
    'license': 'OPL-1',
    'version': '17.0.2.2.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'data/disease_demo.xml',
        'data/demo_specialties.xml',
        'data/demo_persons.xml',

        'views/person_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'views/diagnosis_views.xml',
        'views/menu.xml',
        'views/specialty_views.xml',
        'views/set_personal_doctor_wizard_view.xml',
    ],
    'installable': True,
    'application': True
}
