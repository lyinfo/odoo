# -*- coding: utf-8 -*-
{
    'name': "臺灣地區會計科目表",

    'summary': """
        會科類別/會計科目/稅別""",

    'description': """
        提供臺灣地區現行的會計科目模板以及稅目模板
    """,

    'author': "Kevin Wang",
    'website': "http://www.loyal-info.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization/Account Charts',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'account_chart_type.xml',
        'account_tax.xml',
        'account_chart_general_template.xml',
        'l10n_chart_tw_wizard.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}