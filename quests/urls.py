from django.urls import path

from quests.views import (
    QuestListView,
    QuestDetailView,
    QuestCreateView,
    QuestEditView,
    QuestDeleteView, LatestQuestsView,
)

urlpatterns = [
    path('', QuestListView.as_view(), name='quest-list'),
    path('latest/', LatestQuestsView.as_view(), name='latest-quests'),
    path('create/', QuestCreateView.as_view(), name='quest-create'),
    path('<slug:slug>/', QuestDetailView.as_view(), name='quest-details'),
    path('<slug:slug>/edit/', QuestEditView.as_view(), name='quest-edit'),
    path('<slug:slug>/delete/', QuestDeleteView.as_view(), name='quest-delete'),
]