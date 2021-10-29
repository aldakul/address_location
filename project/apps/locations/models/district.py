from django.db import models
from django.utils.translation import ugettext_lazy as _


class District(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    country = models.ForeignKey(
        'Country',
        models.DO_NOTHING,
        verbose_name=_('ИД Страны'),
    )
    region = models.ForeignKey(
        'Region',
        models.DO_NOTHING,
        verbose_name=_('ИД Региона'),
    )
    district_name_id = models.CharField(
        verbose_name=_('Код Района'),
        max_length=100
    )
    name_ru = models.CharField(
        verbose_name=_('Название Района на русском'),
        max_length=200
    )
    name_kz = models.CharField(
        verbose_name=_('Название Района на казахском'),
        max_length=200
    )

    class Meta:
        managed = False
        verbose_name = _('Район')
        verbose_name_plural = _('Районы')
        db_table = 'address_district'

    def __str__(self):
        return self.id
