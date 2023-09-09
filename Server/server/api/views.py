from django.shortcuts import render
from .serializers import *
from rest_framework import generics

class TelegramUserBaseModel:
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()

class CalculationBaseModel:
    serializer_class = CalculationSerializer
    queryset = Calculation.objects.all()


# Create your views here.
class CreateTelegramUser(TelegramUserBaseModel, generics.CreateAPIView):
    ...
# Create your views here.
class CreateCalculation(CalculationBaseModel, generics.CreateAPIView):
    ...

class GetTelegramUser(TelegramUserBaseModel, generics.RetrieveAPIView):
    lookup_field='external_id'