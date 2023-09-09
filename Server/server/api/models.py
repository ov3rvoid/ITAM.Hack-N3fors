from django.db import models

class TelegramUser(models.Model):
    external_id = models.BigIntegerField(verbose_name='tg id', unique=True)
    username = models.CharField(max_length=256, null=True, verbose_name='Ник в тг')
    first_name = models.CharField(max_length=256, null=True, verbose_name='Имя в тг')
    second_name = models.CharField(max_length=256, null=True, verbose_name='Фамилия в тг')
    age = models.IntegerField(null=True)
    department = models.ForeignKey(to ='Department', on_delete=models.CASCADE)
    course = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self) -> str:
        if self.username is not None:
            return self.username
        return str(self.external_id)
    
class Hobby(models.Model):
    user = models.ForeignKey(to=TelegramUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

class Department(models.Model):
    name = models.CharField(max_length=128)

