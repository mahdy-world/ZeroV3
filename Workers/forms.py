from datetime import datetime
from tkinter import Widget
from django import forms
from .models import *

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        exclude = ['deleted']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control' , }),
            'image' : forms.FileInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'work_type' : forms.Select(attrs={'class':'form-control'}),
            'day_cost' : forms.NumberInput(attrs={'class':'form-control', 'min':0}),
        }
        

class WorkerDeleteForm(forms.ModelForm):
    class Meta:
        fields = ['deleted']
        model = Worker
        widgets = {
            'deleted' : forms.HiddenInput()
        }        
                
        
class WorkerPaymentForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'price', 'worker']
        model = WorkerPayment
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date', 'class':'form-control',
            'placeholder':'تاريخ السحب...', 'id':'date'}),
            'price' : forms.NumberInput(attrs={ 'class':'form-control',
            'placeholder':'المبلغ...', 'id':'price'}),
            # 'admin' : forms.Select(attrs={'class':'form-control',  'placeholder':'المستلم...','id':'recipient', 'id':'admin'}),
        }
        
class WorkerPaymentReportForm(forms.Form):
    from_date = forms.DateField(required=False ,widget=forms.DateInput(attrs={
        'type':'date',
        'name':'from',
        'id':'from_date',
        'class':'form-control',
        'placeholder':'من ...'}),                       
        label= 'من',
        )
         
    to_date = forms.DateField(required=False ,widget=forms.DateInput(attrs={
        'type':'date',
        'name':'to_date',
        'id':'to_date',
        'class':'form-control',
        'placeholder':'الي ...'}),
        label= 'الي',
        )     


class WorkerAttendanceForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'hour_count']
        model = WorkerAttendance
        widgets = {
            'date' :  forms.DateInput(attrs={'type':'date', 'class':'form-control',
            'placeholder':'تاريخ السحب...', 'id':'date'}),
            'hour_count' : forms.Select(attrs={'class':'form-control',
            'placeholder':'عدد الساعات...', 'id':'hours_count'}),
        }
        
 
 
class WorkerProductionForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'quantity']
        model = WorkerProduction
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date', 'class':'form-control',
            'placeholder':'تاريخ الاستلام', 'id':'production_date'}),
            # 'product' : forms.Select(attrs={'type':'text', 'class':'form-control',
            # 'placeholder':' المنتج', 'id':'worker_production'}),
            'quantity' : forms.NumberInput(attrs={ 'class':'form-control', 'placeholder':'الكمية...',
            'id':'worker_quantity'})
        }
                
   