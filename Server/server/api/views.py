from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from random import choice
class TelegramUserBaseModel:
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()


# Create your views here.
class CreateTelegramUser(TelegramUserBaseModel, generics.CreateAPIView):
    lookup_field='external_id'

class ChangeTelegramUser(TelegramUserBaseModel, generics.RetrieveUpdateAPIView):
    lookup_field='external_id'
    
class FindSimUser(APIView):
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()
    def get(self, request, *args, **kwargs):
        id = kwargs.get('external_id')

        user  = TelegramUser.objects.get(external_id=id)
        department = user.department
        users = TelegramUser.objects.filter(department=department).exclude(external_id=id)

        return Response(TelegramUserSerializer(choice(users)).data)
    
class GetTelegramUser(TelegramUserBaseModel, generics.RetrieveAPIView):
    lookup_field='external_id'

class DeleteTelegramUser(TelegramUserBaseModel,generics.DestroyAPIView):
    lookup_field='external_id'

class ListAllTelegramUser(TelegramUserBaseModel,generics.ListAPIView):
    ...