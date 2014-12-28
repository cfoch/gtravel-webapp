# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=80)),
                ('applications_start_date', models.DateField()),
                ('applications_deadline', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('budget', models.DecimalField(max_digits=8, decimal_places=2)),
                ('event_type', models.IntegerField(max_length=1, choices=[(b'Small Event', ((0, b'Hackfest'), (1, b'Other'))), (b'Large Event', ((2, b'GUADEC'), (3, b'GNOME.ASIA'), (4, b'Other')))])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
