# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20141223_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='personal_blog',
        ),
    ]
