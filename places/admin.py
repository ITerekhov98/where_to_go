from django.contrib import admin

from .models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Place)
class PLaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass