from django import forms

from heroes.models import Hero
from quests.models import Quest


class QuestBaseForm(forms.ModelForm):
    class Meta:
        model = Quest
        exclude = ["slug", "created_at"]

        labels = {
            "title": "Quest Title",
            "description": "Description",
            "difficulty": "Difficulty",
            "reward_gold": "Gold Reward",
            "reward_xp": "XP Reward",
            "heroes": "Assigned Heroes",
        }

        widgets = {
            "description": forms.Textarea(attrs={
                "placeholder": "Describe the quest..."
            }),
            "heroes": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["reward_gold"].error_messages["required"] = "Please enter the gold reward."
        self.fields["reward_gold"].error_messages["invalid"] = "Gold reward must be a valid number."

        self.fields["reward_xp"].error_messages["required"] = "Please enter the XP reward."
        self.fields["reward_xp"].error_messages["invalid"] = "XP reward must be a valid number."

        self.fields["heroes"].queryset = Hero.objects.filter(
            is_available_for_quests=True
        ).order_by("name")

        for name, field in self.fields.items():
            if name == "heroes":
                field.widget.attrs["class"] = "form-check-input"
            elif name == "difficulty":
                field.widget.attrs["class"] = "form-select"
            else:
                field.widget.attrs["class"] = "form-control"


class QuestCreateForm(QuestBaseForm):
    pass


class QuestEditForm(QuestBaseForm):
    pass


class QuestDeleteForm(QuestBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True