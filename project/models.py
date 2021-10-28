# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddressCity(models.Model):
    country = models.ForeignKey('AddressCountry', models.DO_NOTHING)
    region = models.ForeignKey('AddressRegion', models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey('AddressDistrict', models.DO_NOTHING, blank=True, null=True)
    city_name_id = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'address_city'


class AddressCountry(models.Model):
    letter_code = models.CharField(max_length=10, blank=True, null=True)
    name_ru = models.CharField(max_length=200, blank=True, null=True)
    name_kz = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_country'


class AddressDistrict(models.Model):
    region = models.ForeignKey('AddressRegion', models.DO_NOTHING)
    district_name_id = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'address_district'


class AddressDistrictInCity(models.Model):
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    region = models.ForeignKey('AddressRegion', models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(AddressDistrict, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(AddressCity, models.DO_NOTHING, blank=True, null=True)
    district_in_city_name_id = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'address_district_in_city'


class AddressHouse(models.Model):
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    region = models.ForeignKey('AddressRegion', models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(AddressDistrict, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(AddressCity, models.DO_NOTHING, blank=True, null=True)
    district_in_city = models.ForeignKey(AddressDistrictInCity, models.DO_NOTHING, blank=True, null=True)
    microdistrict = models.ForeignKey('AddressMicrodistrict', models.DO_NOTHING, blank=True, null=True)
    street = models.ForeignKey('AddressStreet', models.DO_NOTHING, blank=True, null=True)
    new_postcode = models.CharField(max_length=7, blank=True, null=True)
    old_postcode = models.CharField(max_length=6, blank=True, null=True)
    name_ru = models.CharField(max_length=500)
    name_kz = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'address_house'


class AddressMicrodistrict(models.Model):
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    region = models.ForeignKey('AddressRegion', models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(AddressDistrict, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(AddressCity, models.DO_NOTHING, blank=True, null=True)
    district_in_city = models.ForeignKey(AddressDistrictInCity, models.DO_NOTHING, blank=True, null=True)
    microdistrict_name_id = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=500)
    name_kz = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'address_microdistrict'


class AddressRegion(models.Model):
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING, blank=True, null=True)
    letter_code_id = models.CharField(max_length=1)
    region_name_id = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=200, blank=True, null=True)
    name_kz = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_region'


class AddressStreet(models.Model):
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    region = models.ForeignKey(AddressRegion, models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(AddressDistrict, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(AddressCity, models.DO_NOTHING, blank=True, null=True)
    district_in_city = models.ForeignKey(AddressDistrictInCity, models.DO_NOTHING, blank=True, null=True)
    microdistrict = models.ForeignKey(AddressMicrodistrict, models.DO_NOTHING, blank=True, null=True)
    street_name_id = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=200)
    name_kz = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'address_street'
