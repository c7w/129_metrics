# Generated by Django 3.2.5 on 2021-11-30 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField()),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 11, 30, 20, 46, 52, 419122))),
            ],
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 11, 30, 20, 46, 52, 418630))),
            ],
        ),
    ]
