# Generated by Django 3.2.5 on 2021-12-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpareParts', '0012_auto_20211216_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepartssuppliers',
            name='initial_balance',
            field=models.FloatField(default=0, verbose_name='الرصيد الافتتاحي'),
        ),
    ]