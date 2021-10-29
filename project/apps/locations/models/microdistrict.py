from django.db import models
from django.utils.translation import ugettext_lazy as _


class Microdistrict(models.Model):
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
    microdistrict_name_id = models.CharField(
        verbose_name=_('Код Микрорайона'),
        max_length=100
    )
    name_ru = models.CharField(
        verbose_name=_('Название Микрорайона на русском'),
        max_length=500
    )
    name_kz = models.CharField(
        verbose_name=_('Название Микрорайона на казахском'),
        max_length=500
    )

    class Meta:
        managed = False
        verbose_name = _('Микрорайон')
        verbose_name_plural = _('Микрорайоны')
        db_table = 'address_microdistrict'

    def __str__(self):
        return self.id
