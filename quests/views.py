from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from quests.forms import QuestCreateForm, QuestEditForm, QuestDeleteForm
from quests.models import Quest


class QuestListView(ListView):
    model = Quest
    template_name = 'quests/quest-list.html'
    context_object_name = 'quests'


class QuestDetailView(DetailView):
    model = Quest
    template_name = 'quests/quest-details.html'
    context_object_name = 'quest'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class QuestCreateView(CreateView):
    model = Quest
    form_class = QuestCreateForm
    template_name = 'quests/quest-create.html'
    success_url = reverse_lazy('quest-list')


class QuestEditView(UpdateView):
    model = Quest
    form_class = QuestEditForm
    template_name = 'quests/quest-edit.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('quest-details', kwargs={'slug': self.object.slug})


class QuestDeleteView(DeleteView):
    model = Quest
    template_name = 'quests/quest-delete.html'
    success_url = reverse_lazy('quest-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuestDeleteForm(instance=self.object)
        return context