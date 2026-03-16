from django.urls import path

from guilds.views import (
    GuildListView,
    GuildDetailView,
    GuildCreateView,
    GuildEditView,
    GuildDeleteView,
)

urlpatterns = [
    path('', GuildListView.as_view(), name='guild-list'),
    path('create/', GuildCreateView.as_view(), name='guild-create'),
    path('<int:pk>/', GuildDetailView.as_view(), name='guild-details'),
    path('<int:pk>/edit/', GuildEditView.as_view(), name='guild-edit'),
    path('<int:pk>/delete/', GuildDeleteView.as_view(), name='guild-delete'),
]