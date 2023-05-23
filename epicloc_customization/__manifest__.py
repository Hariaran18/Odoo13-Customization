# -*- coding: utf-8 -*-
{
    'name': 'EpicLoc Quotation Customization',
    'version': '1.0',
    'summary': 'EpicLoc Quotation Customization',
    'category': 'Sales',
    'description': """    """,
    'author': 'Hariaran',
    'website': '',
    
    'depends': ['sale_management', 'base', 'product', 'crm', 'sale', 'sale_crm', 'stock','starken-crm'],
    'data': [
              'wizards/import_order_lines_view.xml',
              'views/inherit_sale_order_form.xml',
              'reports/print_option.xml',
              'reports/quotation_sale_order_epicloc.xml',
              'security/ir.model.access.csv',
            ],
    'demo': [],
    'test': [],
    'installable':True,
    'auto_install':False,
    'application':True,
}