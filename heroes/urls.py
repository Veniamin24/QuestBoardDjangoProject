from django.urls import path
from heroes.views import (
    HeroListView,
    HeroDetailView,
    HeroCreateView,
    HeroEditView,
    HeroDeleteView,
)

urlpatterns = [
    path('', HeroListView.as_view(), name='hero-list'),
    path('create/', HeroCreateView.as_view(), name='hero-create'),
    path('<int:pk>/', HeroDetailView.as_view(), name='hero-details'),
    path('<int:pk>/edit/', HeroEditView.as_view(), name='hero-edit'),
    path('<int:pk>/delete/', HeroDeleteView.as_view(), name='hero-delete'),
]