# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=4)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=4)),
                ('sensor_id', models.IntegerField()),
                ('reading', models.IntegerField()),
            ],
        ),
    ]
