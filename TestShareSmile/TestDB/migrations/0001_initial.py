# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import TestDB.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(serialize=False, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('established_year', models.BigIntegerField(max_length=4)),
                ('email_id', models.EmailField(unique=True, max_length=100)),
                ('phone_number', models.BigIntegerField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('locality_ngo', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=250)),
                ('latitude_company', models.DecimalField(max_digits=8, decimal_places=3)),
                ('longitude_company', models.DecimalField(max_digits=8, decimal_places=3)),
                ('date_signed_in', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyCategory',
            fields=[
                ('company_category_id', models.AutoField(serialize=False, primary_key=True)),
                ('company_category_name', models.CharField(max_length=500)),
                ('company_sector', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('event_category_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_category_name', models.CharField(max_length=500)),
                ('event_sector', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('events_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_name', models.CharField(max_length=100)),
                ('date_of_the_event', models.DateField()),
                ('event_description', models.CharField(max_length=1000)),
                ('no_volunteers_expected', models.BigIntegerField()),
                ('no_volunteers_turned_up', models.BigIntegerField()),
                ('email_id', models.EmailField(unique=True, max_length=100)),
                ('phone_number', models.BigIntegerField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('locality_events', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=250)),
                ('date_registered', models.DateField(auto_now=True)),
                ('latitude_event', models.DecimalField(max_digits=8, decimal_places=3)),
                ('longitude_event', models.DecimalField(max_digits=8, decimal_places=3)),
                ('is_active', models.BooleanField()),
                ('company', models.ForeignKey(to='TestDB.Company')),
                ('event_category', models.ForeignKey(to='TestDB.EventCategory')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(serialize=False, primary_key=True)),
                ('headline', models.TextField()),
                ('pub_date', models.DateField()),
                ('crisp_content', models.TextField()),
                ('creator_name', models.CharField(max_length=500)),
                ('curator_name', models.CharField(max_length=500)),
                ('source_content', models.TextField()),
                ('photo', models.ImageField(upload_to=b'')),
                ('video_url', models.CharField(max_length=1000)),
                ('source_link', models.CharField(max_length=1000)),
                ('source_name', models.CharField(max_length=500)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='NGOCategory',
            fields=[
                ('ngo_category_id', models.AutoField(serialize=False, primary_key=True)),
                ('ngo_category_name', models.CharField(max_length=500)),
                ('ngo_sector', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NGOS',
            fields=[
                ('ngo_id', models.AutoField(serialize=False, primary_key=True)),
                ('ngo_name', models.CharField(max_length=100)),
                ('established_year', models.BigIntegerField(max_length=4)),
                ('total_registered_volunteers', models.BigIntegerField()),
                ('impacted_persons', models.BigIntegerField()),
                ('impact_quotient', models.CharField(max_length=300)),
                ('ngo_photo', models.ImageField(null=True, upload_to=TestDB.models.get_image_path, blank=True)),
                ('email_id', models.EmailField(unique=True, max_length=100)),
                ('phone_number', models.BigIntegerField(max_length=12)),
                ('address', models.CharField(max_length=100, null=True)),
                ('locality_ngo', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=250)),
                ('date_signed_in', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField()),
                ('ngo_category', models.ForeignKey(to='TestDB.NGOCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('gender_user', models.CharField(max_length=10)),
                ('email_id', models.EmailField(unique=True, max_length=100)),
                ('phone_number', models.BigIntegerField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('locality_user', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=250)),
                ('date_signed_in', models.DateField(auto_now=True)),
                ('latitude_user', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('longitude_user', models.DecimalField(null=True, max_digits=8, decimal_places=3)),
                ('is_volunteer', models.BooleanField()),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_registered', models.BooleanField()),
                ('has_attended', models.BooleanField()),
                ('impact_score', models.BigIntegerField()),
                ('events', models.ForeignKey(to='TestDB.Events')),
                ('users', models.ForeignKey(to='TestDB.Users')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='ngo',
            field=models.ForeignKey(to='TestDB.NGOS'),
        ),
        migrations.AddField(
            model_name='company',
            name='company_category',
            field=models.ForeignKey(to='TestDB.CompanyCategory'),
        ),
    ]
