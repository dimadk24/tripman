# Generated by Django 3.2 on 2021-04-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0008_auto_20200418_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'экскурсия',
                'verbose_name_plural': 'экскурсии',
            },
        ),
        migrations.AddField(
            model_name='tripdefinition',
            name='excursions',
            field=models.ManyToManyField(blank=True, to='main.Excursion',
                                         verbose_name='Экскурсии'),
        ),
    ]
