from django import forms
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
        }

        widgets = {
            "description": forms.Textarea(attrs={
                "placeholder": "Describe the quest..."
            }),
            "difficulty": forms.Select(attrs={
                "placeholder": "Choose a difficulty..."
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["reward_gold"].error_messages["required"] = "Please enter the gold reward."
        self.fields["reward_gold"].error_messages["invalid"] = "Gold reward must be a positive number."

        self.fields["reward_xp"].error_messages["required"] = "Please enter the XP reward."
        self.fields["reward_xp"].error_messages["invalid"] = "XP reward must be a positive number."


class QuestCreateForm(QuestBaseForm):
    pass


class QuestEditForm(QuestBaseForm):
    pass


class QuestDeleteForm(QuestBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True