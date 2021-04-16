from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название")
    county = models.CharField(max_length=40, verbose_name="Страна")

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"

    def __str__(self):
        return self.name
