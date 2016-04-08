# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import TestDB.models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0003_auto_20160308_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='causes',
            name='cause_image',
            field=models.ImageField(null=True, upload_to=TestDB.models.get_cause_image_path, blank=True),
        ),
    ]
