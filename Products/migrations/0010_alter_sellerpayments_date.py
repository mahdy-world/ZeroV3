# Generated by Django 3.2.5 on 2022-04-19 00:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 2, 23, 47, 534101), verbose_name='التاريخ'),
        ),
    ]
