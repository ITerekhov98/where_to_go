from django.contrib import admin

from .models import Place


@admin.register(Place)
class PLaceAdmin(admin.ModelAdmin):
    pass