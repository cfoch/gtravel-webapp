# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='blog',
            field=models.URLField(null=True, verbose_name=b'Blog'),
            preserve_default=True,
        ),
    ]
