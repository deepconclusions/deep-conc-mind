from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    # path(route="/", view=include('allauth.urls')),
    path(route="blogs", view=views.blog, name="blogs"),
    path(route="blog/<int:blog_id>", view=views.blogDetail, name="blog_detail"),
]
