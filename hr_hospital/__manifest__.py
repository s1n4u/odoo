{
    'name': 'Hospital Management',
    'summary': '',
    'author': 's1n',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.2.2.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [

        'security/ir.model.access.csv',

        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',

    ],
    'demo': [

    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],


}

