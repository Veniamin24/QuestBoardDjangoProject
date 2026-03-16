from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from guilds.forms import GuildCreateForm, GuildEditForm, GuildDeleteForm
from guilds.models import Guild


class GuildListView(ListView):
    model = Guild
    template_name = 'guilds/guild-list.html'
    context_object_name = 'guilds'


class GuildDetailView(DetailView):
    model = Guild
    template_name = 'guilds/guild-details.html'
    context_object_name = 'guild'


class GuildCreateView(CreateView):
    model = Guild
    form_class = GuildCreateForm
    template_name = 'guilds/guild-create.html'
    success_url = reverse_lazy('guild-list')


class GuildEditView(UpdateView):
    model = Guild
    form_class = GuildEditForm
    template_name = 'guilds/guild-edit.html'

    def get_success_url(self):
        return reverse_lazy('guild-details', kwargs={'pk': self.object.pk})


class GuildDeleteView(DeleteView):
    model = Guild
    template_name = 'guilds/guild-delete.html'
    success_url = reverse_lazy('guild-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GuildDeleteForm(instance=self.object)
        return context