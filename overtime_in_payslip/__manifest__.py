# -*- coding: utf-8 -*-
{
    'name': 'Overtime in Payslip',

    'version': '16',
    'summary': 'Overtime in Payslip',
    'author': 'DeeB',
    'website': "",
    'category': 'human resource',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_payroll'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/bonus_type.xml',
        'views/employee_bonus.xml',
        'views/hr_payslip.xml',
        'wizard/bonus_deduction_report_wizard_view.xml',
        'views/employee_bonus_deduction_report_doc.xml',
        'report/employee_bonus_deduction_report.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        "web.assets_frontend": [
            # to add scss and js here
        ],
        "web.assets_qweb": [
            # to add templates here
        ],
    },
    'images': ['static/description/icon.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
}

