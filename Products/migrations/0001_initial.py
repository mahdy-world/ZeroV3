# Generated by Django 3.2.5 on 2022-06-12 00:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الاضافة')),
                ('name', models.CharField(max_length=50, verbose_name='اسم اللون')),
                ('code', models.CharField(max_length=20, verbose_name='كود اللون')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='تاريخ الاضافة')),
                ('name', models.CharField(max_length=50, verbose_name='اسم الموديل')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='صورة الموديل')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='وزن الموديل')),
                ('time', models.FloatField(blank=True, null=True, verbose_name='زمن الموديل')),
                ('cost', models.FloatField(blank=True, max_length=15, null=True, verbose_name='التكلفة')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='سعر البيع')),
                ('size', models.IntegerField(blank=True, choices=[('', '------------'), (1, 'S'), (2, 'M'), (3, 'L'), (3, 'XL'), (3, 'XXL')], default=0, null=True, verbose_name='المقاس')),
                ('category', models.IntegerField(blank=True, choices=[('', '------------'), (1, 'شبابي'), (2, 'حريمي'), (3, 'اطفالي اولادي'), (4, 'اطفالي بناتي')], default=0, null=True, verbose_name='التصنيف')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='الكمية')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='اسم التاجر')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='رقم الهاتف')),
                ('nation_no', models.CharField(blank=True, max_length=14, null=True, verbose_name='الرقم القومي')),
                ('initial_balance_debit', models.FloatField(default=0, verbose_name='القيمة الافتتاحية')),
                ('initial_balance_type', models.IntegerField(choices=[(1, 'للتاجر'), (2, 'علي التاجر')], default=0, verbose_name='نوع القيمة الافتتاحية')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف')),
                ('agreement', models.CharField(blank=True, max_length=500, null=True, verbose_name='اتفاق مسبق')),
            ],
        ),
        migrations.CreateModel(
            name='SellerPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_value', models.FloatField(default=0.0, verbose_name='القيمة المدفوعة')),
                ('paid_type', models.IntegerField(choices=[(1, 'التاجر يدفع لك'), (2, 'أنت تدفع للتاجر')], default=0, verbose_name='نوع الدفع')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 6, 12, 2, 19, 33, 423085), verbose_name='التاريخ')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.productsellers', verbose_name='التاجر')),
            ],
        ),
    ]
