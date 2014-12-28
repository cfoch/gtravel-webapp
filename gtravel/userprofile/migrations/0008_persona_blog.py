# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_remove_persona_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='blog',
            field=models.URLField(default=datetime.datetime(2014, 12, 23, 16, 12, 49, 594333, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
