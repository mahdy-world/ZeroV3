# Generated by Django 3.2.5 on 2021-12-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treasury', '0002_bankaccount_hometreasury'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktreasury',
            name='initial_balance',
        ),
        migrations.AddField(
            model_name='worktreasury',
            name='balance',
            field=models.FloatField(default=0, verbose_name='الرصيد'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.FloatField(default=0.0, verbose_name='الرصيد'),
        ),
        migrations.AlterField(
            model_name='hometreasury',
            name='balance',
            field=models.FloatField(default=0.0, verbose_name='الرصيد'),
        ),
    ]