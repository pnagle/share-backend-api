# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0006_auto_20160326_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsors',
            old_name='cause_id',
            new_name='cause',
        ),
        migrations.RemoveField(
            model_name='causes',
            name='sponsor',
        ),
    ]
