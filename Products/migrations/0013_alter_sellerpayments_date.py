# Generated by Django 3.2.5 on 2022-05-18 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0012_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 21, 6, 22, 559068), verbose_name='التاريخ'),
        ),
    ]
