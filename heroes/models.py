from django.db import models

from common.mixins import CreatedAtMixin
from guilds.models import Guild
from heroes.choices import HeroClassChoices


class Hero(CreatedAtMixin):
    name = models.CharField(max_length=50)
    hero_class = models.CharField(
        max_length=20,
        choices=HeroClassChoices
    )
    level = models.PositiveIntegerField()
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        related_name="heroes",
        null=True,
        blank=True
    )
    is_available_for_quests = models.BooleanField(default=True)

    def __str__(self):
        return self.name
