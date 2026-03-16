from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from heroes.forms import HeroCreateForm, HeroEditForm, HeroDeleteForm
from heroes.models import Hero


class HeroListView(ListView):
    model = Hero
    template_name = 'heroes/hero-list.html'
    context_object_name = 'heroes'


class HeroDetailView(DetailView):
    model = Hero
    template_name = 'heroes/hero-details.html'
    context_object_name = 'hero'


class HeroCreateView(CreateView):
    model = Hero
    form_class = HeroCreateForm
    template_name = 'heroes/hero-create.html'
    success_url = reverse_lazy('hero-list')


class HeroEditView(UpdateView):
    model = Hero
    form_class = HeroEditForm
    template_name = 'heroes/hero-edit.html'

    def get_success_url(self):
        return reverse_lazy('hero-details', kwargs={'pk': self.object.pk})


class HeroDeleteView(DeleteView):
    model = Hero
    template_name = 'heroes/hero-delete.html'
    success_url = reverse_lazy('hero-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HeroDeleteForm(instance=self.object)
        return context