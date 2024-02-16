from django.contrib.admin import *

from .models import Commentary

@register(Commentary)
class ComAdmin(ModelAdmin):
    list_display=('id', 'user')
    list_display_links=('id', 'user')