from rest_framework import serializers
from .models import *


class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = '__all__'

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'