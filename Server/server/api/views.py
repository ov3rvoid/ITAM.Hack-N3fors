from .serializers import *
from rest_framework import generics
from rest_framework.response import Response

class TelegramUserBaseModel:
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()


# Create your views here.
class CreateTelegramUser(TelegramUserBaseModel, generics.CreateAPIView):
    lookup_field='external_id'

class ChangeTelegramUser(TelegramUserBaseModel, generics.RetrieveUpdateAPIView):
    lookup_field='external_id'
    
class FindSimUser(TelegramUserBaseModel, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        external_id = kwargs.get('external_id')
        return Response(self.serializer_class(TelegramUser.objects.all()).data)
    
class GetTelegramUser(TelegramUserBaseModel, generics.RetrieveAPIView):
    lookup_field='external_id'

class DeleteTelegramUser(TelegramUserBaseModel,generics.DestroyAPIView):
    lookup_field='external_id'

class ListAllTelegramUser(TelegramUserBaseModel,generics.ListAPIView):
    ...