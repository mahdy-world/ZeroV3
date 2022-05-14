# Generated by Django 3.2.5 on 2021-12-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treasury', '0005_alter_bankaccounttransactions_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccounttransactions',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'مشتريات'), (2, 'مبيعات'), (3, 'سحب يدوي'), (4, 'ايداع يدوي')], default=0, verbose_name='نوع العملية'),
        ),
        migrations.AlterField(
            model_name='hometreasurytransactions',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'مشتريات'), (2, 'مبيعات'), (3, 'سحب يدوي'), (4, 'ايداع يدوي')], default=0, verbose_name='نوع العملية'),
        ),
        migrations.AlterField(
            model_name='worktreasurytransactions',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'مشتريات'), (2, 'مبيعات'), (3, 'سحب يدوي'), (4, 'ايداع يدوي')], default=0, verbose_name='نوع العملية'),
        ),
    ]