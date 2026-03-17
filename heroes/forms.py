from django import forms

from guilds.models import Guild
from heroes.models import Hero


class HeroBaseForm(forms.ModelForm):
    class Meta:
        model = Hero
        exclude = ['created_at']
        labels = {
            'name': 'Hero Name',
            'hero_class': 'Class',
            'level': 'Level',
            'guild': 'Guild',
            'is_available_for_quests': 'Available for quests',
        }
        help_texts = {
            'name': 'Choose a fearsome name.',
            'level': 'Choose a level between 1 and 100.',
            'guild': 'Choose your guild wisely.',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ragnar'}),
            'level': forms.NumberInput(attrs={'placeholder': '25'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["guild"].queryset = Guild.objects.order_by("name")
        self.fields["guild"].empty_label = "No guild."
        self.fields["name"].error_messages["required"] = "You can't be unnamed."
        self.fields["level"].error_messages["invalid"] = "Hero level must be a positive number."

        for field_name, field in self.fields.items():
            if field_name == "is_available_for_quests":
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class HeroCreateForm(HeroBaseForm):
    pass


class HeroEditForm(HeroBaseForm):
    pass


class HeroDeleteForm(HeroBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True

