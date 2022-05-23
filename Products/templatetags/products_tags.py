from django import template
from django.db.models import Sum

register = template.Library()
from Products.models import *


@register.simple_tag(name='sellers_debit')
def sellers_debit(seller_id):
    seller = ProductSellers.objects.get(id=seller_id)
    seller_payments_from = SellerPayments.objects.filter(seller__id=seller_id, paid_type=1)
    seller_payments_to = SellerPayments.objects.filter(seller__id=seller_id, paid_type=2)
    if seller:
        initial_debit = seller.initial_balance_debit
    else:
        initial_debit = 0

    if seller_payments_from:
        payments_from = seller_payments_from.aggregate(sum=Sum('paid_value')).get('sum')
    else:
        payments_from = 0

    if seller_payments_to:
        payments_to = seller_payments_to.aggregate(sum=Sum('paid_value')).get('sum')
    else:
        payments_to = 0

    if seller.initial_balance_type == 1:
        sum = (payments_from - payments_to) + initial_debit
    else:
        sum = (payments_from - payments_to) - initial_debit
    return float(sum)