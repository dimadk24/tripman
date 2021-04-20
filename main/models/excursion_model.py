from django.db import models


class Excursion(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    times_included = models.IntegerField(default=0,
                                         verbose_name="Путевок с экскурсией")
    times_visited = models.IntegerField(default=0,
                                        verbose_name="Посещений экскурсии")

    class Meta:
        verbose_name = "экскурсия"
        verbose_name_plural = "экскурсии"

    def __str__(self):
        return self.name
