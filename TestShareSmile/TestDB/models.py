from django.db import models
import os
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


def get_profile_picture_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


def get_cause_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


def get_sponsor_logo_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True)
    gender_user = models.CharField(max_length=10, null=True)
    email_id = models.EmailField(max_length=100, unique=True, null=True)
    phone_number = models.BigIntegerField(max_length=12, null=True)
    address = models.CharField(max_length=100, null=True)
    locality_user = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=250, null=True)
    date_signed_in = models.DateField(auto_now=True, null=True)
    latitude_user = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    longitude_user = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    is_volunteer = models.BooleanField()
    total_distance = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    profile_picture = models.ImageField(upload_to=get_profile_picture_image_path, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='users')
    highlighted = models.TextField()


class CausesCategory(models.Model):
    cause_category_id = models.AutoField(primary_key=True)
    cause_category_name = models.CharField(max_length=500)


class SponsorType(models.Model):
    sponsor_type_id = models.BigIntegerField()
    sponsor_type_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.sponsor_type_name


class Sponsors(models.Model):
    sponsor_id = models.BigIntegerField()
    # causes = models.ForeignKey('Causes', related_name='causes', null=True)
    sponsor_type = models.ForeignKey('SponsorType')
    sponsor_company = models.ForeignKey('Company', blank=True, null=True)
    sponsor_ngo = models.ForeignKey('NGOS', blank=True, null=True)
    sponsor_logo = models.ImageField(upload_to=get_sponsor_logo_image_path, blank=True, null=True)
    partnered_on = models.DateTimeField(null=True)


class Causes(models.Model):
    cause_id = models.AutoField(primary_key=True)
    cause_title = models.CharField(max_length=200)
    cause_brief = models.CharField(max_length=300)
    cause_description = models.CharField(max_length=500, null=True)
    cause_image = models.ImageField(upload_to=get_cause_image_path, blank=True, null=True)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2)
    cause_category = models.ForeignKey('CausesCategory')
    sponsors = models.ManyToManyField('Sponsors', blank=True, null=True)
    create_time = models.DateField(null=True)
    amount = models.BigIntegerField()
    is_active = models.BooleanField()

    def __unicode__(self):
        return self.cause_title


class Runs(models.Model):
    run_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users')
    cause_id = models.ForeignKey('Causes')
    start_location_lat = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    start_location_long = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    avg_speed = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    end_location_lat = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    end_location_long = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    distance = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    peak_speed = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    calories_burnt = models.DecimalField(max_digits=8, decimal_places=3, null=True)


class PartnerType(models.Model):
    partner_type_id = models.BigIntegerField()
    partner_type_name = models.CharField(max_length=200)


class Partners(models.Model):
    partner_id = models.BigIntegerField()
    cause_id = models.ForeignKey('Causes')
    partner_type_id = models.ForeignKey('PartnerType')
    partnered_on = models.DateTimeField(null=True)


def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = self.linenos and 'table' or False
    options = self.title and {'title': self.title} or {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Users, self).save(*args, **kwargs)


class EventCategory(models.Model):
    event_category_id = models.AutoField(primary_key=True)
    event_category_name = models.CharField(max_length=500)
    event_sector = models.CharField(max_length=500)


class Events(models.Model):
    events_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    event_category = models.ForeignKey('EventCategory')
    ngo = models.ForeignKey('NGOS')
    company = models.ForeignKey('Company')
    date_of_the_event = models.DateField()
    event_description = models.CharField(max_length=1000)
    no_volunteers_expected = models.BigIntegerField()
    no_volunteers_turned_up = models.BigIntegerField()
    email_id = models.EmailField(max_length=100,unique=True)
    phone_number = models.BigIntegerField(max_length=12)
    address = models.CharField(max_length=100)
    locality_events = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    date_registered = models.DateField(auto_now=True)
    latitude_event = models.DecimalField(max_digits=8, decimal_places=3)
    longitude_event = models.DecimalField(max_digits=8, decimal_places=3)
    is_active = models.BooleanField()


class NGOCategory(models.Model):
    ngo_category_id = models.AutoField(primary_key=True)
    ngo_category_name = models.CharField(max_length=500)
    ngo_sector = models.CharField(max_length=500)


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class NGOS(models.Model):
    ngo_id = models.AutoField(primary_key=True)
    ngo_name = models.CharField(max_length=100)
    ngo_category = models.ForeignKey('NGOCategory')
    established_year = models.BigIntegerField(max_length=4)
    total_registered_volunteers = models.BigIntegerField()
    impacted_persons = models.BigIntegerField()
    impact_quotient = models.CharField(max_length=300)
    ngo_photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    email_id = models.EmailField(max_length=100,unique=True)
    phone_number = models.BigIntegerField(max_length=12)
    address = models.CharField(max_length=100,null=True)
    locality_ngo = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    date_signed_in = models.DateField(auto_now=True)
    is_active = models.BooleanField()


class CompanyCategory(models.Model):
    company_category_id = models.AutoField(primary_key=True)
    company_category_name = models.CharField(max_length=500)
    company_sector = models.CharField(max_length=500)

    def __unicode__(self):
        return self.company_category_name


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_category = models.ForeignKey('CompanyCategory')
    established_year = models.BigIntegerField(max_length=4, null=True)
    email_id = models.EmailField(max_length=100,unique=True,null=True)
    phone_number = models.BigIntegerField(max_length=12)
    address = models.CharField(max_length=100,null=True)
    locality_ngo = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    latitude_company = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    longitude_company = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    date_signed_in = models.DateField(auto_now=True)
    is_active = models.BooleanField()

    def __unicode__(self):
        return self.company_name


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    headline = models.TextField()
    pub_date = models.DateField()
    crisp_content = models.TextField()
    creator_name = models.CharField(max_length=500)
    curator_name = models.CharField(max_length=500)
    source_content = models.TextField()
    photo = models.ImageField()
    video_url = models.CharField(max_length=1000)
    source_link = models.CharField(max_length=1000)
    source_name = models.CharField(max_length=500)
    is_active = models.BooleanField()


class Volunteers(models.Model):
    users = models.ForeignKey('Users')
    events = models.ForeignKey('Events')
    is_registered = models.BooleanField()
    has_attended = models.BooleanField()
    impact_score = models.BigIntegerField()
