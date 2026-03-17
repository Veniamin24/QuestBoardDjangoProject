from django.urls import path
from heroes.views import (
    HeroListView,
    HeroDetailView,
    HeroCreateView,
    HeroEditView,
    HeroDeleteView, TopHeroesView,
)

urlpatterns = [
    path('', HeroListView.as_view(), name='hero-list'),
    path('top/', TopHeroesView.as_view(), name='top-heroes'),
    path('create/', HeroCreateView.as_view(), name='hero-create'),
    path('<int:pk>/', HeroDetailView.as_view(), name='hero-details'),
    path('<int:pk>/edit/', HeroEditView.as_view(), name='hero-edit'),
    path('<int:pk>/delete/', HeroDeleteView.as_view(), name='hero-delete'),
]