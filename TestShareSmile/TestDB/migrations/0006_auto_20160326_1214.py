# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0005_auto_20160325_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsors',
            old_name='sponsor_type_id',
            new_name='sponsor_type',
        ),
        migrations.AddField(
            model_name='causes',
            name='sponsor',
            field=models.ForeignKey(to='TestDB.Sponsors', null=True),
        ),
    ]
