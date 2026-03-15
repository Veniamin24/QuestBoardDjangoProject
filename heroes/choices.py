from django.db import models


class HeroClassChoices(models.TextChoices):
    WARRIOR = "Warrior", "Warrior"
    MAGE = "Mage", "Mage"
    ROGUE = "Rogue", "Rogue"
    PALADIN = "Paladin", "Paladin"
    DRUID = "Druid", "Druid"
    HUNTER = "Hunter", "Hunter"
    SHAMAN = "Shaman", "Shaman"