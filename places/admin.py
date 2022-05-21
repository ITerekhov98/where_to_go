from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, \
                                 SortableInlineAdminMixin, \
                                 SortableAdminBase

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('order_number', 'image', 'image_prewiew',)
    readonly_fields = ['image_prewiew']

    def image_prewiew(self, obj):
        width = obj.image.width
        height = obj.image.height
        if height > 200:
            ratio = 200 / height
            height *= ratio
            width *= ratio
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=width,
            height=height,
            )
        )

    def get_extra(self, request, obj=None, **kwargs):
        return 0


@admin.register(Place)
class PLaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ('order_number', 'image', 'image_prewiew',)
    list_display = ('order_number', 'image', 'image_prewiew',)
    readonly_fields = ['image_prewiew']

    def image_prewiew(self, obj):
        width = obj.image.width
        height = obj.image.height
        if height > 200:
            ratio = 200 / height
            height *= ratio
            width *= ratio
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=width,
            height=height,
            )
        )
