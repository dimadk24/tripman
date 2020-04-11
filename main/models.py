from django.db import models


# Create your models here.


class TripDefinition(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Имя')
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='Цена')
    startDate = models.DateField(verbose_name='Дата старта')
    endDate = models.DateField(verbose_name='Дата конца')
    services = models.ManyToManyField('Service', verbose_name='Сервисы')


class Service(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Имя')
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='Цена')


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    discount = models.DecimalField(max_digits=5, decimal_places=2,
                                   verbose_name='Скидка')


class Trip(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               verbose_name='Клиент')
    trip_definition = models.ForeignKey(TripDefinition,
                                        on_delete=models.CASCADE,
                                        verbose_name='Путевка')
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='Цена')
    sell_date = models.DateField(verbose_name='Дата продажи')
