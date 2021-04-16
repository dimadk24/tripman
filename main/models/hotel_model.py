from django.db import models


class Hotel(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=30)
    city = models.ForeignKey("City", verbose_name="Город",
                             on_delete=models.CASCADE)
    address = models.CharField(max_length=50, verbose_name="Адрес")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "отель"
        verbose_name_plural = "отель"

    def __str__(self):
        return self.name
