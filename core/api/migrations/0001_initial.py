# Generated by Django 4.0.4 on 2022-07-24 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=255, verbose_name='player')),
                ('wins', models.IntegerField(default=0, verbose_name='wins')),
                ('loss', models.IntegerField(default=0, verbose_name='loss')),
                ('points', models.IntegerField(default=0, verbose_name='points')),
                ('day_played', models.DateField(default=datetime.date(2022, 7, 24))),
                ('played', models.IntegerField(default=0, verbose_name='played')),
            ],
        ),
    ]
