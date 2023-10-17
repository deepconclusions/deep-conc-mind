from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "profile"

urlpatterns = [
    # path(route="/", view=include('allauth.urls')),
    path(route="profiles", view=views.profiles, name="profiles"),
    path(route="profile/<int:profile_id>", view=views.profileDetail, name="profile_detail"),
]
