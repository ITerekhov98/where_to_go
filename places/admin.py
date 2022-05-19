from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'image_prewiew', 'order_number',)
    readonly_fields = ['image_prewiew']

    def image_prewiew(self, obj):
        width = obj.image.width
        height=obj.image.height
        if height > 200:
            ratio = 200 / height
            height *= ratio
            width *= ratio
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=width,
            height=height,
            )
        )

@admin.register(Place)
class PLaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('image', 'image_prewiew', 'order_number',)
    readonly_fields = ['image_prewiew']

    def image_prewiew(self, obj):
        width = obj.image.width
        height=obj.image.height
        if height > 200:
            ratio = 200 / height
            height *= ratio
            width *= ratio
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=width,
            height=height,
            )
        )
