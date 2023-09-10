from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'external_id',
        'username',
        'first_name',
        'second_name',
        'age',
        'department',
        'course',
        'description',
        'gender',
        'photo'
    )
    list_per_page = 50
    list_display_links = list_display
    


admin.site.register(TelegramUser, UserAdmin)