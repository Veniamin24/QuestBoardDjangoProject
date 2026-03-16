from django.contrib import admin
from django.urls import path, include

from common.views import HomePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('heroes/', include('heroes.urls')),
    path('guilds/', include('guilds.urls')),
    path('quests/', include('quests.urls')),
]