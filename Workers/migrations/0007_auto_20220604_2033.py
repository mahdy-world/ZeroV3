# Generated by Django 3.2.5 on 2022-06-04 18:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Workers', '0006_auto_20220604_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 4, 18, 33, 23, 899242, tzinfo=utc), verbose_name='تاريخ الحضور'),
        ),
        migrations.AlterField(
            model_name='workerpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 4, 18, 33, 23, 899242, tzinfo=utc), verbose_name='تاريخ السحب'),
        ),
        migrations.AlterField(
            model_name='workerproduction',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 4, 18, 33, 23, 899242, tzinfo=utc), verbose_name='تاريخ الاستلام'),
        ),
    ]
