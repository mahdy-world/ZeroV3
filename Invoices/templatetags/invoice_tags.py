from django import template
from django.db.models import Sum

register = template.Library()
from Invoices.models import *

@register.simple_tag(name='invoice_products')
def invoice_products(inv_id):
    return InvoiceItem.objects.filter(invoice__id=inv_id)


@register.simple_tag(name='invoice_products_val')
def invoice_products_val(inv_id):
    return InvoiceItem.objects.filter(invoice__id=inv_id).aggregate(sum=Sum('total_price')).get('sum')


@register.simple_tag(name='invoice_saved')
def invoice_saved(inv_id):
    return Invoice.objects.filter(id=inv_id, saved=True)


@register.simple_tag(name='profit_decimal')
def Profit_Decimal(num):
    number = num

    if number:
        numbe = "{:g}".format(number)
    else:
        numbe = number

    if '.' in str(numbe):
        numb = str(numbe).split('.')
        if len(numb[1]) == 1:
            numm = "{:.1f}".format(float(numbe))
        else:
            numm = "{:.2f}".format(float(numbe))
    else:
        numm = numbe

    return numm