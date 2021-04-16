from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Имя')
    price = models.IntegerField(verbose_name='Цена (руб)')

    class Meta:
        verbose_name = 'дополнительный сервис'
        verbose_name_plural = 'дополнительные сервисы'

    def __str__(self):
        return f'{self.name} ({self.price} руб)'
