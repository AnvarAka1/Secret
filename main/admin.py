from django.contrib import admin
from .models import *


class TagsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class GalleryInline(admin.StackedInline):
    model = Gallery
    fieldsets = (
        (None, {
            'fields': ('image',),
        }),
    )


class PostAdmin(admin.ModelAdmin):
    list_display = ['title',]
    inlines = [
        GalleryInline,
    ]


admin.site.register(Tags, TagsAdmin)
admin.site.register(Post, PostAdmin)
