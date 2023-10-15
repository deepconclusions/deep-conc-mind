from django.contrib import admin
from .models import (Chat, Secrets)

# Register your models here.
admin.site.register(model_or_iterable=[Chat, Secrets])