from django.db import models
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
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
    city_name_id = models.CharField(
        verbose_name=_('Код города'),
        max_length=100
    )
    name_ru = models.CharField(
        verbose_name=_('Название Города на русском'),
        max_length=200
    )
    name_kz = models.CharField(
        verbose_name=_('Название Города на казахском'),
        max_length=200
    )

    class Meta:
        managed = False
        verbose_name = _('Город')
        verbose_name_plural = _('Города')
        db_table = 'address_city'

    def __str__(self):
        return self.id
