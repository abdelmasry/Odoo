{
    'name': 'Digizilla Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Custom module for managing Digizilla data',
    'description': """
        This module creates a custom model Digizilla with specific fields and views.
    """,
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'report/digizilla_report.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}