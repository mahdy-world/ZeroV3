from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from Products.models import *
# Create your models here.

invoice_choices = (
    (1, "فاتورة مبيعات"),
    (2, "فاتورة مرتجع مبيعات"),
    (3, "بيان أسعار"),
)

class Invoice(models.Model):
    date = models.DateField(default=now, verbose_name='التاريخ')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='منشئ الفاتورة')
    invoice_type = models.IntegerField(choices=invoice_choices, default=0, verbose_name='نوع الفاتورة')
    seller = models.ForeignKey(ProductSellers, on_delete=models.SET_NULL, null=True, verbose_name='التاجر')
    customer = models.CharField(max_length=255, verbose_name='العميل')
    total = models.FloatField(default=0.0, verbose_name='قيمة الفاتورة')
    discount = models.FloatField(default=0.0, verbose_name='الخصم')
    overall = models.FloatField(default=0.0, verbose_name='الإجمالي')
    comment = models.TextField(null=True, blank=True, verbose_name="ملاحظات")
    saved = models.BooleanField(default=False, verbose_name='حفظ')
    deleted = models.BooleanField(default=False, verbose_name='حذف')
    return_inv_id = models.IntegerField(default=0, verbose_name='رقم الفاتورة الأصلية')

    def __str__(self):
        return str(self.id)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='الفاتورة')
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='الصنف')
    unit_price = models.FloatField(default=0.0, verbose_name='سعر البيع')
    quantity = models.FloatField(default=1.0, verbose_name='الكمية')
    total_price = models.FloatField(default=0.0, verbose_name='إجمالي')
    deleted = models.BooleanField(default=False, verbose_name='حذف المنتج من الفاتورة')

    def __str__(self):
        return str(self.invoice.id)


class InvoiceItemDetails(models.Model):
    invoice_item = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE, verbose_name='عنصر الفاتورة')
    quantity = models.FloatField(default=1.0, verbose_name='الكمية')
    undo = models.FloatField(default=0, verbose_name='الكمية المرتجعة')
    balance = models.FloatField(default=1.0, verbose_name='الرصيد')
    purchase_price = models.FloatField(default=0.0, verbose_name='سعر البيع')

    def __str__(self):
        return str(self.invoice_item.invoice.id)