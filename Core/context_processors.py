from Core.models import SystemInformation
from Factories.models import Factory
from Products.models import Product, ProductSellers
from Invoices.models import *
from django.db.models import F
from Products.templatetags.products_tags import sellers_debit as SellerDebit
from Workers.models import Worker



def allcontext(request):
    info = SystemInformation.objects.filter(id=1)
    factorys = Factory.objects.filter(deleted=False)
    products = Product.objects.filter(deleted=False)
    sellers = ProductSellers.objects.filter(deleted=False)
    workers = Worker.objects.filter(deleted=False)

    invoices_notify = Invoice.objects.filter(saved=False)
    products_notify = Product.objects.filter(price__lt=F('cost'))

    notification_count = invoices_notify.count() + products_notify.count()

    context = { 
        'info':info,
        'factorys' : factorys,
        'products':products,
        'sellers':sellers,
        'workers':workers,
        'invoices_notify':invoices_notify,
        'products_notify':products_notify,
        'notification_count':notification_count,
    }
    return context