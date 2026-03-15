from django.db import models

from common.mixins import CreatedAtMixin
from heroes.models import Hero
from quests.choices import QuestDifficultyChoices


class Quest(CreatedAtMixin):
    title = models.CharField(max_length=50)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=20,
        choices=QuestDifficultyChoices
    )
    reward_gold = models.PositiveIntegerField()
    reward_xp = models.PositiveIntegerField()
    heroes = models.ManyToManyField(
        Hero,
        related_name="quests"
    )

    def __str__(self):
        return self.title