# Generated by Django 3.2.5 on 2021-12-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinessuppliers',
            name='credit_or_debit',
            field=models.IntegerField(choices=[(1, 'لك عند المورد'), (2, 'عليك للمورد')], default=0, verbose_name='لك أم عليك'),
        ),
    ]
