from django.contrib import admin
from .models import (Author, Blog)

# Register your models here.
admin.site.register(model_or_iterable=[Author, Blog])

