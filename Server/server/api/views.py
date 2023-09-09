from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TelegramUserBaseModel:
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()


# Create your views here.
class CreateTelegramUser(TelegramUserBaseModel, generics.CreateAPIView):
    ...


class GetTelegramUser(TelegramUserBaseModel, generics.RetrieveAPIView):
    lookup_field='external_id'