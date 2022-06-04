# Generated by Django 3.2.5 on 2022-06-01 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Treasury', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SparePartsNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='اسم الصنف')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SparePartsSuppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='اسم المورد')),
                ('phone', models.CharField(max_length=11, verbose_name='رقم الهاتف')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف')),
            ],
        ),
        migrations.CreateModel(
            name='SparePartsTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='الاسم')),
                ('deleted', models.BooleanField(default=False, verbose_name='مسح')),
            ],
        ),
        migrations.CreateModel(
            name='SparePartsWarehouses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='اسم المخزن')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SparePartsWarehouseTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0.0, verbose_name='الكمية')),
                ('price_cost', models.FloatField(default=0.0, verbose_name='سعر الشراء')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartsnames', verbose_name='المنتجات')),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartswarehouses', verbose_name='المخزن')),
            ],
        ),
        migrations.CreateModel(
            name='SparePartsOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50, null=True, verbose_name='رقم الطلب')),
                ('order_date', models.DateField(null=True, verbose_name='تاريخ الطلب')),
                ('order_deposit_value', models.FloatField(default=0, null=True, verbose_name='قيمة العربون')),
                ('order_deposit_date', models.DateField(null=True, verbose_name='تاريخ دفع العربون')),
                ('order_rest_date', models.DateField(null=True, verbose_name='تاريخ دفع باقي المبلغ')),
                ('order_receipt_date', models.DateField(null=True, verbose_name='تاريخ استلام البضاعة')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف')),
                ('order_supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartssuppliers', verbose_name='المورد')),
            ],
        ),
        migrations.CreateModel(
            name='SparePartsOrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(default=0, null=True, verbose_name='الكمية')),
                ('product_price', models.FloatField(default=0, null=True, verbose_name='سعر الشراء')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف')),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartsnames', verbose_name='المنتج')),
                ('product_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartsorders', verbose_name='الطلبية')),
            ],
        ),
        migrations.CreateModel(
            name='SparePartsOrderOperations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_date', models.DateTimeField(null=True, verbose_name='تاريخ العملية')),
                ('operation_type', models.IntegerField(choices=[(1, 'دفع عربون'), (2, 'دفع باقي المبلغ'), (3, 'دفع مبلغ تخليص البضاعة'), (4, 'استلام البضاعة'), (5, 'دفع الضرائب')], default=0, verbose_name='نوع العملية')),
                ('operation_value', models.FloatField(default=0, verbose_name='قيمة العملية')),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartsorders', verbose_name='رقم الطلب')),
                ('treasury_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Treasury.worktreasury', verbose_name='الخزنة المستخدمة')),
                ('warehouse_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartswarehouses', verbose_name='المخزن المستخدم')),
            ],
        ),
        migrations.AddField(
            model_name='sparepartsnames',
            name='spare_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpareParts.sparepartstypes', verbose_name='نوع قطعة الغيار'),
        ),
    ]
