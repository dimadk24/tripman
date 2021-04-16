from django.db import models


class TripDefinition(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Имя")
    price = models.IntegerField(verbose_name="Цена (руб)")
    location = models.CharField(max_length=50, verbose_name="Населенный пункт")
    start_date = models.DateField(verbose_name="Дата отправления")
    end_date = models.DateField(verbose_name="Дата возвращения")
    services = models.ManyToManyField("Service", verbose_name="Сервисы",
                                      blank=True)
    excursions = models.ManyToManyField("Excursion", verbose_name="Экскурсии",
                                        blank=True)

    class Meta:
        verbose_name = "путевка"
        verbose_name_plural = "путевки"

    def __str__(self):
        return f"{self.name} ({self.price} руб)"
