# Generated by Django 3.2 on 2021-04-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0015_alter_trip_sell_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='times_included',
            field=models.IntegerField(default=0,
                                      verbose_name='Путевок с экскурсией'),
        ),
    ]
