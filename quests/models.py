from django.db import models
from django.utils.text import slugify

from common.mixins import CreatedAtMixin
from heroes.models import Hero
from quests.choices import QuestDifficultyChoices


class Quest(CreatedAtMixin):
    title = models.CharField(max_length=50, unique=True)
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
    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]