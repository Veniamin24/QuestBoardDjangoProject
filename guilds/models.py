from django.core.validators import  MaxValueValidator
from django.db import models

from common.mixins import CreatedAtMixin


class Guild(CreatedAtMixin):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    level = models.PositiveIntegerField(validators=[MaxValueValidator(50)])
    members = models.PositiveIntegerField(validators=[MaxValueValidator(20)])
    description = models.TextField(blank=True, null=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
