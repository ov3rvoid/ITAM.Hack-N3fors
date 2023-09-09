from django.contrib import admin
from .models import *
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         'external_id',
#         'username',
#         'first_name',
#         'second_name'
#     )
#     list_per_page = 50
#     list_display_links = list_display
    

# class CalculationAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Calculation._meta.get_fields()]
#     list_per_page = 50
#     list_display_links = list_display


# admin.site.register(TelegramUser, UserAdmin)
# admin.site.register(Calculation, CalculationAdmin)