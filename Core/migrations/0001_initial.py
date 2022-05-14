# Generated by Django 3.2.5 on 2021-12-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='اسم صاحب النظام')),
                ('phone', models.IntegerField(max_length=12, null=True, verbose_name='رقم الموبيل')),
                ('address', models.CharField(max_length=150, null=True, verbose_name='العنوان')),
            ],
        ),
    ]