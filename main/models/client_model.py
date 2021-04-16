from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    discount = models.IntegerField(default=0, verbose_name='Скидка (%)')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return self.name
