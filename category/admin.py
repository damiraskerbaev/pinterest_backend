from django.contrib.admin import *

from .models import Category

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('name',)