# Generated by Django 3.2.5 on 2022-05-14 12:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Workers', '0004_alter_workerattendance_hour_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='worker_type',
            field=models.IntegerField(choices=[(1, 'عامل ارضية'), (2, 'عامل خياطة'), (3, 'عامل مكوي'), (4, 'عامل مكينة'), (5, 'عامل عادي'), (6, 'عامل انتاج')], verbose_name='نوع العامل'),
        ),
        migrations.AlterField(
            model_name='workerattendance',
            name='hour_count',
            field=models.IntegerField(blank=True, choices=[(1, '6'), (2, '8'), (3, '12'), (4, '18')], null=True, verbose_name='عدد الساعات'),
        ),
        migrations.CreateModel(
            name='WorkerProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2022, 5, 14), verbose_name='تاريخ الاستلام')),
                ('quantity', models.FloatField(default=0, verbose_name='الكمية')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المسئول')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Workers.worker', verbose_name='العامل')),
            ],
        ),
    ]
