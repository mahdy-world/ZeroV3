from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['date', 'seller']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class InvoiceSaveForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['total', 'discount', 'overall', 'comment']
        widgets = {
            'total': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inv_total', 'readonly': 'readonly'}),
            'overall': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'inv_overall', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discount'].widget.attrs = {'min': '0', 'max': self['total'].value(), 'id': 'inv_discount'}


class InvoiceBackForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['saved']
        widgets = {
            'saved': forms.HiddenInput(),
        }


class InvoiceDeleteForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['deleted']
        widgets = {
            'deleted': forms.HiddenInput(),
        }


class InvoiceProductsForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['item', 'unit_price', 'quantity', 'total_price']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control', 'id': 'item'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'unit_price'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'total_price', 'readonly': 'readonly'}),
        }


class InvoiceProductsFormUpdate(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['item', 'unit_price', 'quantity', 'total_price']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control', 'id': 'item', 'readonly': 'readonly'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'id': 'unit_price'}),
            'total_price': forms.HiddenInput(attrs={'class': 'form-control', 'min': '1', 'id': 'total_price', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(InvoiceProductsFormUpdate, self).__init__(*args, **kwargs)
        self.fields['item'].empty_label = None


class InvoiceProductsDeleteForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['deleted']
        widgets = {
            'deleted': forms.HiddenInput(),
        }