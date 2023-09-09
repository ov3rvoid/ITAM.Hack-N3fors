from django.urls import *
from api.views import *

urlpatterns = [
    path('create_telegram_user', CreateTelegramUser.as_view()),
    path('get_telegram_user/<int:external_id>', GetTelegramUser.as_view()),
    path('change_telegram_user/<int:external_id>', ChangeTelegramUser.as_view()),
    path('delete_telegram_user/<int:external_id>', DeleteTelegramUser.as_view()),
    path('list_all_telegram_user',ListAllTelegramUser.as_view()),
]