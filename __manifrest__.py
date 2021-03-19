# -*- coding: utf-8 -*-
{
    'name': "Scheduled_reminders",
    'summary': """Scheduled reminders model""",
    'description': """Managing car information""",
    'author': "nguyennha",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/scheduled_reminders_views.xml',
        'views/cron_remind.xml',
    ],
}