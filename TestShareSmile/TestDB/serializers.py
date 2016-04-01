from rest_framework import serializers
from .models import Users,Causes,CausesCategory,Partners,NGOS,Company,PartnerType,Sponsors,SponsorType
from django.contrib.auth.models import User
import os


class UsersSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    device_id = serializers.IntegerField()
    first_name = serializers.CharField( max_length=100)
    last_name = serializers.CharField(max_length=100)
    gender_user = serializers.CharField(max_length=10)
    email_id = serializers.EmailField(max_length=100)
    phone_number = serializers.IntegerField()
    address = serializers.CharField(style={'base_template': 'textarea.html'})
    locality_user = serializers.CharField(style={'base_template': 'textarea.html'})
    city = serializers.CharField(style={'base_template': 'textarea.html'})
    state = serializers.CharField(style={'base_template': 'textarea.html'})
    country = serializers.CharField(style={'base_template': 'textarea.html'})
    isVolunteer = serializers.BooleanField(required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.device_id = validated_data.get('device_id', instance.device_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender_user = validated_data.get('gender_user', instance.gender_user)
        instance.email_id = validated_data.get('email_id', instance.email_id)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.locality_user = validated_data.get('locality_user', instance.locality_user)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.isVolunteer = validated_data.get('isVolunteer', instance.isVolunteer)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


class UserInterfaceSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=Users.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'users')


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('company_name', )


class NGOSerializer(serializers.ModelSerializer):

    class Meta:
        model = NGOS
        fields = ('ngo_name', )


class PartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partners
        fields = ('partner_id', 'cause_id', 'partner_type_id', 'partnered_on')

    partner_type = serializers.HyperlinkedModelSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        model = PartnerType
        fields = 'partner_type_name'


class SponsorTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsorType
        fields = ('sponsor_type_name', )


class SponsorsSerializer(serializers.ModelSerializer):

    sponsor_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='sponsor_type_name'
    )
    # sponsor_name = serializers.SerializerMethodField()
    sponsor_company = serializers.SlugRelatedField(
        read_only=True,
        slug_field='company_name'
    )

    sponsor_ngo = serializers.SlugRelatedField(
        read_only=True,
        slug_field='ngo_name',

    )

    sponsor_logo = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Sponsors
        fields = ('sponsor_id', 'sponsor_type', 'sponsor_company', 'sponsor_ngo', 'sponsor_logo')


class CausesSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    cause_title = serializers.CharField(required=True, allow_blank=False, max_length=200)
    cause_brief = serializers.CharField(required=False, allow_blank=True, max_length=300)
    cause_description = serializers.CharField(max_length=500)
    conversion_rate = serializers.IntegerField()

    cause_category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='cause_category_name',

    )

    sponsors = SponsorsSerializer(many=True)
    cause_brief = serializers.CharField(allow_blank=True, max_length=300)
    cause_image = serializers.ImageField(max_length=None, allow_empty_file=True)
    is_active = serializers.BooleanField()
