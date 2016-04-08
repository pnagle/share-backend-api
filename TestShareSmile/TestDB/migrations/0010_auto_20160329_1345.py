# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0009_auto_20160329_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsors',
            name='sponsor_company',
            field=models.ForeignKey(blank=True, to='TestDB.Company', null=True),
        ),
        migrations.AddField(
            model_name='sponsors',
            name='sponsor_ngo',
            field=models.ForeignKey(blank=True, to='TestDB.NGOS', null=True),
        ),
        migrations.AlterField(
            model_name='causes',
            name='sponsors',
            field=models.ManyToManyField(to='TestDB.Sponsors', null=True, blank=True),
        ),
    ]
