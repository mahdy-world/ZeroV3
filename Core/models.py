from email.policy import default
from django.db import models


# Create your models here.

class SystemInformation(models.Model):
    logo = models.ImageField(null=True, blank=True, verbose_name="شعارالنظام")
    name = models.CharField(null=True, max_length=50, verbose_name="اسم النظام")
    type = models.CharField(null=True, max_length=50, verbose_name="نوع النظام")
    manage = models.CharField(null=True, max_length=50, verbose_name="إدارة")
    phone = models.CharField(null=True, max_length=11, verbose_name="هاتف 1")
    phone2 = models.CharField(null=True, max_length=11, verbose_name="هاتف 2")
    address = models.CharField(max_length=150, null=True, verbose_name="العنوان")
    
    def __str__(self):
        return self.name
    
    
class Modules(models.Model):
    machine_active  = models.BooleanField(default=True, verbose_name="تنشيط المكينات")
    spareParts_active = models.BooleanField(default=True, verbose_name="تنشيط قطع الغيار")
    treasurty_active = models.BooleanField(default=True, verbose_name="تنشيط الخزينة")
    factory_active = models.BooleanField(default=True, verbose_name="تنشيط المصانع")
    products_active = models.BooleanField(default=True, verbose_name="تنشيط المنتجات")
    wools_active = models.BooleanField(default=True, verbose_name="تنشيط مخازن الصوف ")
    worker_active = models.BooleanField(default=True, verbose_name="تنشيط مخازن العمال ")
    
    def __str__(self):
        return "عناصر النظام"    