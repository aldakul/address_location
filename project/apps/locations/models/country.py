from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractTimeTrackable


class Country(AbstractTimeTrackable):
    letter_code = models.CharField(
        max_length=10,
        verbose_name=_('ISO CODE')
    )
    name_ru = models.CharField(
        max_length=10,
        verbose_name=_('Название на русском')
    )
    name_kz = models.PositiveIntegerField(
        verbose_name=_('Название на казахском')
    )

    class Meta:
        verbose_name = _('Страна')
        verbose_name_plural = _('Страны')

    def __str__(self):
        return self.id
