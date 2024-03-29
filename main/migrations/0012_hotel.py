# Generated by Django 3.2 on 2021-04-16 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0011_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('address',
                 models.CharField(max_length=50, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('city',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='main.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'отель',
                'verbose_name_plural': 'отель',
            },
        ),
        migrations.AddField(
            model_name='tripdefinition',
            name='hotel',
            field=models.ForeignKey(default=1,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='main.hotel', verbose_name='Отель'),
            preserve_default=False,
        ),
    ]
