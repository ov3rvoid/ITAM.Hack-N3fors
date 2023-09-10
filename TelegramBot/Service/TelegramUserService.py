import requests
from Config import PROXY
import json

class TelegramUserService:
    def CreateTelegramUser(external_id, username, first_name, second_name):
        requests.post(PROXY+'create_telegram_user', data=json.dumps({
            "external_id": external_id,
            "username": username,
            "first_name": first_name,
            "age": 18,
            "course": 1,
            "description": "",
            "photo": None,
            "department": None
        }), headers={
            "Content-type": "application/json",
        },)
    def GetTelegramUser(external_id):
        return requests.get(PROXY+'get_telegram_user/'+ str(external_id),).json()
    
    def DeleteTelegramUser(external_id):
        data = requests.get(PROXY+'get_telegram_user/'+str(external_id),).json()

    def ChangeTelegramUsers(external_id, data):
        data = data.as_dict()
        data['external_id'] = external_id
        requests.put(PROXY+'change_telegram_user/'+str(external_id), data=json.dumps({
            "external_id": data['external_id'],
            "first_name": data['name'],
            "age": int(data['age']),
            "course": int(data['course']),
            "description": data['description'],
            "gender": int(data['gender']),
            "photo": None,
            "department": data['department']
        }), headers={
            "Content-type": "application/json",
        },)
