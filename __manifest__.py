# -*- coding: utf-8 -*-

{
    'name': "Odoo show company only partner",
    'summary': """Make sure users can see only the partners belonging to the same company""",
    'description': """
        This Module:
            - 
    """,
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',
    'author': "Mounir lahsini",
    'website': "https://github.com/matteopolleschi/odoo_show_company_only_partner",
    'depends': [
        'base',
        'contacts'
        ],
    'data': [
        'security/security.xml',
        'views/res_partner.xml',
        ],
    'installable': True,
}
