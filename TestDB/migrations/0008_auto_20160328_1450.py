# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0007_auto_20160328_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsors',
            name='cause',
        ),
        migrations.AddField(
            model_name='sponsors',
            name='causes',
            field=models.ForeignKey(related_name='causes', to='TestDB.Causes', null=True),
        ),
    ]
