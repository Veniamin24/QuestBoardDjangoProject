from django.db import models


class QuestDifficultyChoices(models.TextChoices):
    EASY = "Easy", "Easy"
    MEDIUM = "Medium", "Medium"
    HARD = "Hard", "Hard"
    NIGHTMARE = "Nightmare", "Nightmare"