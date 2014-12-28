# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_persona_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='blog',
        ),
    ]
