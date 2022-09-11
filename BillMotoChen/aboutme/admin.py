from django.contrib import admin

# Register your models here.

from .models import Career, Pieces

admin.site.register(Career)
admin.site.register(Pieces)