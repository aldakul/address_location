from django.db import models
from django.utils.translation import ugettext_lazy as _


class DistrictInCity(models.Model):
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
    district_in_city_name_id = models.CharField(
        verbose_name=_('Код Района в Городе'),
        max_length=100,
    )
    name_ru = models.CharField(
        verbose_name=_('Название Района в Городе на русском'),
        max_length=200
    )
    name_kz = models.CharField(
        verbose_name=_('Название Района в Городе на казахском'),
        max_length=200
    )

    class Meta:
        managed = False
        verbose_name = _('Района в Городе')
        verbose_name_plural = _('Районы в Городе')
        db_table = 'address_city'

    def __str__(self):
        return self.id
