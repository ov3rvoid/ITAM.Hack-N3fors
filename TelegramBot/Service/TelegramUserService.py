import requests
from Config import PROXY
import json

class TelegramUserService:
    def CreateTelegramUser(external_id, username, first_name, second_name):
        requests.post(PROXY+'create_telegram_user', data=json.dumps({
            'external_id': external_id,
            'username': username,
            'first_name': first_name,
            'second_name': second_name,
        }), headers={
            "Content-type": "application/json",
        },)
    def GetTelegramUser(external_id):
        return requests.get(PROXY+'get_telegram_user/'+ str(external_id)).json()
    
    def DeleteTelegramUser(external_id):
        data = requests.get(PROXY+'get_telegram_user/'+str(external_id)).json()

    def UpdateTelegramUsers(external_id):
        requests.patch(PROXY+'change_telegram_user/'+str(external_id)).json()
