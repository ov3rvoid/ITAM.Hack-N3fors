from django.db import models

class TelegramUser(models.Model):
    external_id = models.BigIntegerField(verbose_name='tg id', unique=True)
    username = models.CharField(max_length=256, null=True, verbose_name='Ник в тг')
    first_name = models.CharField(max_length=256, null=True, verbose_name='Имя в тг')
    second_name = models.CharField(max_length=256, null=True, verbose_name='Фамилия в тг')
    age = models.IntegerField(default=18)
    department = models.TextField(null=True, blank=True)
    course = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self) -> str:
        if self.username is not None:
            return self.username
        return str(self.external_id)
    
class Hobby(models.Model):
    name = models.CharField(max_length=128)
    user =  models.ForeignKey(to=TelegramUser, on_delete= models.CASCADE)

class Department(models.Model):
    name = models.CharField(max_length=128)