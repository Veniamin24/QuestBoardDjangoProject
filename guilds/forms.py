from django import forms

from guilds.models import Guild


class GuildBaseForm(forms.ModelForm):
    class Meta:
        model = Guild
        exclude = ['created_at']
        labels = {
            'name': 'Guild Name',
            'country': 'Country',
            'level': 'Guild Level',
            'members': 'Members Count',
            'description': 'Description',
            'is_open': 'Available to join',
        }

class GuildCreateForm(GuildBaseForm):
    pass


class GuildEditForm(GuildBaseForm):
    pass


class GuildDeleteForm(GuildBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True