# Generated by Django 3.2.5 on 2022-06-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systeminformation',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='شعارالنظام'),
        ),
    ]