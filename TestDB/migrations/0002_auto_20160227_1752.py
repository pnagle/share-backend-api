# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import TestDB.models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Causes',
            fields=[
                ('cause_id', models.AutoField(serialize=False, primary_key=True)),
                ('cause_title', models.CharField(max_length=200)),
                ('cause_description', models.CharField(max_length=500, null=True)),
                ('conversion_rate', models.BigIntegerField()),
                ('create_time', models.DateField(null=True)),
                ('amount', models.BigIntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CausesCategory',
            fields=[
                ('cause_category_id', models.AutoField(serialize=False, primary_key=True)),
                ('cause_category_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Executors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('executor_id', models.BigIntegerField()),
                ('partnered_on', models.DateTimeField(null=True)),
                ('cause_id', models.ForeignKey(to='TestDB.Causes')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('executor_type_id', models.BigIntegerField()),
                ('executor_type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Runs',
            fields=[
                ('run_id', models.AutoField(serialize=False, primary_key=True)),
                ('start_location_lat', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('start_location_long', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('avg_speed', models.DecimalField(null=True, max_digits=8, decimal_places=2)),
                ('end_location_lat', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('end_location_long', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('distance', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('peak_speed', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('calories_burnt', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('cause_id', models.ForeignKey(to='TestDB.Causes')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='device_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=TestDB.models.get_profile_picture_image_path, blank=True),
        ),
        migrations.AddField(
            model_name='users',
            name='total_amount',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='total_distance',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
        ),
        migrations.AddField(
            model_name='runs',
            name='user_id',
            field=models.ForeignKey(to='TestDB.Users'),
        ),
        migrations.AddField(
            model_name='executors',
            name='executor_type_id',
            field=models.ForeignKey(to='TestDB.ExecutorType'),
        ),
        migrations.AddField(
            model_name='causes',
            name='cause_category_id',
            field=models.ForeignKey(to='TestDB.CausesCategory'),
        ),
    ]
