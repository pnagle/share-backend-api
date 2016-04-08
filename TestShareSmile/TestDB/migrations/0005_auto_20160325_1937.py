# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0004_causes_cause_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='causes',
            old_name='cause_category_id',
            new_name='cause_category',
        ),
        migrations.AlterField(
            model_name='users',
            name='device_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='middle_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
