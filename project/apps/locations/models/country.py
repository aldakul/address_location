from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    letter_code = models.CharField(
        verbose_name=_('ISO CODE'),
        max_length=10,
        blank=True,
        null=True
    )
    name_ru = models.CharField(
        verbose_name=_('Название Страны на русском'),
        max_length=200,
        blank=True,
        null=True
    )
    name_kz = models.CharField(
        verbose_name=_('Название Страны на казахском'),
        max_length=200,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        verbose_name = _('Страна')
        verbose_name_plural = _('Страны')
        db_table = 'address_country'

    def __str__(self):
        return self.id
