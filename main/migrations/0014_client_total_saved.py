# Generated by Django 3.2 on 2021-04-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0013_remove_tripdefinition_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='total_saved',
            field=models.IntegerField(default=0,
                                      verbose_name='Всего сэкономлено (руб)'),
        ),
    ]