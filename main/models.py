from django.db import models


# Create your models here.


class TripDefinition(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Имя')
    price = models.IntegerField(verbose_name='Цена (руб)')
    location = models.CharField(max_length=50, verbose_name='Населенный пункт')
    start_date = models.DateField(verbose_name='Дата отправления')
    end_date = models.DateField(verbose_name='Дата возвращения')
    services = models.ManyToManyField('Service', verbose_name='Сервисы',
                                      blank=True)

    class Meta:
        verbose_name = 'путевка'
        verbose_name_plural = 'путевки'

    def __str__(self):
        return f'{self.name} ({self.price} руб)'


class Service(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Имя')
    price = models.IntegerField(verbose_name='Цена (руб)')

    class Meta:
        verbose_name = 'дополнительный сервис'
        verbose_name_plural = 'дополнительные сервисы'

    def __str__(self):
        return f'{self.name} ({self.price} руб)'


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    discount = models.IntegerField(default=0, verbose_name='Скидка (%)')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return self.name


class Trip(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               verbose_name='Клиент')
    trip_definition = models.ForeignKey(TripDefinition,
                                        on_delete=models.CASCADE,
                                        verbose_name='Путевка')
    price = models.IntegerField(verbose_name='Цена (руб)')
    sell_date = models.DateField(verbose_name='Дата продажи')

    class Meta:
        verbose_name = 'путешествие'
        verbose_name_plural = 'путешествия'

    def __str__(self):
        return (f'Путешествие клиента "{self.client}" по путевке '
                + f'"{self.trip_definition}"')
