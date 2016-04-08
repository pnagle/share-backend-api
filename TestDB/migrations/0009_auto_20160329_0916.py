# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import TestDB.models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0008_auto_20160328_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsors',
            name='causes',
        ),
        migrations.AddField(
            model_name='causes',
            name='sponsors',
            field=models.ManyToManyField(to='TestDB.Sponsors'),
        ),
        migrations.AddField(
            model_name='sponsors',
            name='sponsor_logo',
            field=models.ImageField(null=True, upload_to=TestDB.models.get_sponsor_logo_image_path, blank=True),
        ),
    ]
