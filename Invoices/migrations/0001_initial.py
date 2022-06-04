# Generated by Django 3.2.5 on 2022-06-01 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='التاريخ')),
                ('invoice_type', models.IntegerField(choices=[(1, 'فاتورة مبيعات'), (2, 'فاتورة مرتجع مبيعات'), (3, 'مبيعات مستقلة')], default=0, verbose_name='نوع الفاتورة')),
                ('customer', models.CharField(max_length=255, verbose_name='العميل')),
                ('total', models.FloatField(default=0.0, verbose_name='قيمة الفاتورة')),
                ('discount', models.FloatField(default=0.0, verbose_name='الخصم')),
                ('overall', models.FloatField(default=0.0, verbose_name='الإجمالي')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='ملاحظات')),
                ('saved', models.BooleanField(default=False, verbose_name='حفظ')),
                ('close', models.BooleanField(default=False, verbose_name='اغلاق')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف')),
                ('return_inv_id', models.IntegerField(default=0, verbose_name='رقم الفاتورة الأصلية')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='منشئ الفاتورة')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.productsellers', verbose_name='التاجر')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.FloatField(default=0.0, verbose_name='سعر البيع')),
                ('quantity', models.FloatField(default=1.0, verbose_name='الكمية')),
                ('unit', models.IntegerField(choices=[(1, 'قطعة'), (12, 'دستة')], default=0, verbose_name='الوحدة')),
                ('total_price', models.FloatField(default=0.0, verbose_name='إجمالي')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف المنتج من الفاتورة')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='التاريخ')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Invoices.invoice', verbose_name='الفاتورة')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.product', verbose_name='الصنف')),
            ],
        ),
    ]
