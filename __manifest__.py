{
    'name': "Default Modules Modifier",
    'version': '12.0.1.0.0',
    'depends': ['base','mail','sale'],
    'author': "Sathir Plus, Codeso LK",
    'license':"AGPL-3",
    'category': 'Extra Tools',
    'description': "Modules for Modifying Default Modules",
    # data files always loaded at installation
    'data': [
        'sales_mod.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}