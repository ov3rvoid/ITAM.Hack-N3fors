from django.urls import *
from api.views import *

urlpatterns = [
    path('create_telegram_user', CreateTelegramUser.as_view()),
    path('get_telegram_user/<int:external_id>', GetTelegramUser.as_view()),
]