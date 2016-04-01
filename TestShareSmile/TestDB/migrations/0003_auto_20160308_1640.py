# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0002_auto_20160227_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('partner_id', models.BigIntegerField()),
                ('partnered_on', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sponsor_id', models.BigIntegerField()),
                ('partnered_on', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sponsor_type_id', models.BigIntegerField()),
                ('sponsor_type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='ExecutorType',
            new_name='PartnerType',
        ),
        migrations.RemoveField(
            model_name='executors',
            name='cause_id',
        ),
        migrations.RemoveField(
            model_name='executors',
            name='executor_type_id',
        ),
        migrations.RenameField(
            model_name='partnertype',
            old_name='executor_type_id',
            new_name='partner_type_id',
        ),
        migrations.RenameField(
            model_name='partnertype',
            old_name='executor_type_name',
            new_name='partner_type_name',
        ),
        migrations.AddField(
            model_name='causes',
            name='cause_brief',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='causes',
            name='conversion_rate',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='email_id',
            field=models.EmailField(max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='established_year',
            field=models.BigIntegerField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='latitude_company',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='company',
            name='locality_ngo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='longitude_company',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='country',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_signed_in',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email_id',
            field=models.EmailField(max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender_user',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='locality_user',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.BigIntegerField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='total_amount',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.DeleteModel(
            name='Executors',
        ),
        migrations.AddField(
            model_name='sponsors',
            name='cause_id',
            field=models.ForeignKey(to='TestDB.Causes'),
        ),
        migrations.AddField(
            model_name='sponsors',
            name='sponsor_type_id',
            field=models.ForeignKey(to='TestDB.SponsorType'),
        ),
        migrations.AddField(
            model_name='partners',
            name='cause_id',
            field=models.ForeignKey(to='TestDB.Causes'),
        ),
        migrations.AddField(
            model_name='partners',
            name='partner_type_id',
            field=models.ForeignKey(to='TestDB.PartnerType'),
        ),
    ]
