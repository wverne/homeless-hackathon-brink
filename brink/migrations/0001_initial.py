# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelpRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('type', models.CharField(choices=[(b'slp', b'Rough Sleeping'), (b'beg', b'Begging'), (b'asb', b'Anti-Social Behaviour'), (b'hlt', b'Health'), (b'saf', b'Safety')], max_length=3)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
    ]