# Generated by Django 3.2.5 on 2022-06-03 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 14, 55, 52, 144055), verbose_name='التاريخ'),
        ),
    ]