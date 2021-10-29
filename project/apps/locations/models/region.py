from django.db import models
from django.utils.translation import ugettext_lazy as _


class Region(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    country = models.ForeignKey(
        'Country',
        models.DO_NOTHING,
        verbose_name=_('ИД Страны'),
        blank=True,
        null=True

    )
    letter_code_id = models.CharField(
        verbose_name=_('Буквенный Код Региона'),
        max_length=1
    )
    region_name_id = models.CharField(
        verbose_name=_('Код Региона'),
        max_length=100,
        blank=True,
        null=True
    )
    name_ru = models.CharField(
        verbose_name=_('Название Региона на русском'),
        max_length=200,
        blank=True,
        null=True
    )
    name_kz = models.CharField(
        verbose_name=_('Название Региона на казахском'),
        max_length=200,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        db_table = 'address_region'

    def __str__(self):
        return self.id
