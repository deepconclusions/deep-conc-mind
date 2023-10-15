from django.contrib import admin
from .models import (Chat, Secret)

# Register your models here.
admin.site.register(model_or_iterable=[Chat, Secret])