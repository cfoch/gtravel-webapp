# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20141223_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='blog',
            new_name='personal_blog',
        ),
    ]
