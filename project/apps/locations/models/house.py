from django.db import models
from django.utils.translation import ugettext_lazy as _


class House(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    country = models.ForeignKey(
        'Country',
        models.DO_NOTHING,
        verbose_name=_('ИД Страны')
    )
    region = models.ForeignKey(
        'Region',
        models.DO_NOTHING,
        verbose_name=_('ИД Региона'),
    )
    district = models.ForeignKey(
        'District',
        models.DO_NOTHING,
        verbose_name=_('ИД Района'),
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        'City',
        models.DO_NOTHING,
        verbose_name=_('ИД города'),
        blank=True,
        null=True
    )
    district_in_city = models.ForeignKey(
        'DistrictInCity',
        models.DO_NOTHING,
        verbose_name=_('ИД Района в Городе'),
        blank=True,
        null=True
    )
    microdistrict = models.ForeignKey(
        'Microdistrict',
        models.DO_NOTHING,
        verbose_name=_('ИД Микрорайона'),
        blank=True,
        null=True
    )
    street = models.ForeignKey(
        'Street',
        models.DO_NOTHING,
        verbose_name=_('ИД Улицы'),
        blank=True,
        null=True
    )
    new_postcode = models.CharField(
        verbose_name=_('Новый почтовый индекс'),
        max_length=7,
        blank=True,
        null=True
    )
    old_postcode = models.CharField(
        verbose_name=_('Старый почтовый индекс'),
        max_length=6,
        blank=True,
        null=True
    )
    name_ru = models.CharField(
        verbose_name=_('Название Дома на русском'),
        max_length=500
    )
    name_kz = models.CharField(
        verbose_name=_('Название Дома на казахском'),
        max_length=500
    )

    class Meta:
        managed = False
        verbose_name = _('Дом')
        verbose_name_plural = _('Дома')
        db_table = 'address_house'

    def __str__(self):
        return self.id
