# Generated by Django 3.2.5 on 2022-04-19 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wool', '0002_auto_20220419_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wool',
            name='company',
        ),
        migrations.RemoveField(
            model_name='wool',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='wool',
            name='wool_type',
        ),
    ]