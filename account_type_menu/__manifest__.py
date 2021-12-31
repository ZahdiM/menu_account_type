# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Account Type Menu',
    'version': '14.0.1.0',
    'category': 'accounting',
    'summary': 'Account type menu',
    'website': 'https://www.mediodconsulting.com',
    'description': """""",
    'sequence': -100,
    'depends': ['account_accountant'],
    'data': [
        'views/account_type_menu.xml'
    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}