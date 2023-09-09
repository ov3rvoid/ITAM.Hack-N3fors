from django.db import models

class Calculation(models.Model):
    user = models.ForeignKey(to='TelegramUser', on_delete=models.CASCADE)
    A_min = models.FloatField(null=True, blank=True)
    A_max = models.FloatField(null=True, blank=True)
    dB = models.FloatField(null=True, blank=True)
    result = models.FloatField()   
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

class TelegramUser(models.Model):
    external_id = models.BigIntegerField(verbose_name='tg id', unique=True)
    username = models.CharField(max_length=256, null=True, verbose_name='Ник в тг')
    first_name = models.CharField(max_length=256, null=True, verbose_name='Имя в тг')
    second_name = models.CharField(max_length=256, null=True, verbose_name='Фамилия в тг')
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=100)
    course = models.PositiveIntegerField()
    hobby = models.ForeignKey('self', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self) -> str:
        if self.username is not None:
            return self.username
        return str(self.external_id)