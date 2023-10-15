from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include

app_name = 'mind'

urlpatterns = [
    path('', view=views.mind, name='chat'),
    path(route='delete', view=views.deleteChat, name='delete'),
]