from django.db import models


class Trip(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE,
                               verbose_name="Клиент")
    trip_definition = models.ForeignKey(
        'TripDefinition', on_delete=models.CASCADE, verbose_name="Путевка"
    )
    price = models.IntegerField(verbose_name="Цена (руб)")
    sell_date = models.DateField(verbose_name="Дата продажи", blank=True)

    class Meta:
        verbose_name = "путешествие"
        verbose_name_plural = "путешествия"

    def __str__(self):
        return (
            f'Путешествие клиента "{self.client}" по путевке '
            + f'"{self.trip_definition}"'
        )
