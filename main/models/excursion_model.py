from django.db import models


class Excursion(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")

    class Meta:
        verbose_name = "экскурсия"
        verbose_name_plural = "экскурсии"

    def __str__(self):
        return self.name
