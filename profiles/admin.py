from django.contrib import admin
from .models import (Profile, Skill, Qualification)

# Register your models here.

admin.site.register(model_or_iterable=[Profile, Skill, Qualification])
