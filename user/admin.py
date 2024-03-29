from django.contrib.admin import *

from .models import User

@register(User)
class UserAdmin(ModelAdmin):
    list_display=('id', 'username','first_name', 'last_name')
    list_display_links=('id', 'username', 'first_name', 'last_name')
    