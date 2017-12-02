# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demosky', '0015_auto_20171201_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='sensormine',
            name='dateandtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensormine',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
