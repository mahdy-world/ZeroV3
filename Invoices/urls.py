from django.urls import path 
from .views import *

app_name = 'Invoices'
urlpatterns = [
   path('InvoiceList/', InvoiceList.as_view(), name="InvoiceList"),
   path('InvoiceTrashList/', InvoiceTrashList.as_view(), name="InvoiceTrashList"),
   path('InvoiceCreate/', InvoiceCreate.as_view(), name="InvoiceCreate"),
   path('InvoiceUpdate/<int:pk>/', InvoiceUpdate.as_view(), name="InvoiceUpdate"),
   path('InvoiceSave/<int:pk>/', InvoiceSave.as_view(), name="InvoiceSave"),
   path('InvoiceBack/<int:pk>/', InvoiceBack.as_view(), name="InvoiceBack"),
   path('InvoiceRestore/<int:pk>/', InvoiceRestore.as_view(), name="InvoiceRestore"),
   path('InvoiceSuperDelete/<int:pk>/', InvoiceSuperDelete.as_view(), name="InvoiceSuperDelete"),
   path('InvoiceDelete/<int:pk>/', InvoiceDelete.as_view(), name="InvoiceDelete"),
   path('InvoiceDetail/<int:pk>/', InvoiceDetail, name="InvoiceDetail"),
   path('AddProductInvoice/<int:pk>/', AddProductInvoice, name='AddProductInvoice'),
   path('InvoiceProductsUpdate/<int:pk>/<int:id>/', InvoiceProductsUpdate.as_view(), name='InvoiceProductsUpdate'),
   path('InvoiceProductsDelete/<int:pk>/<int:id>/', InvoiceProductsDelete.as_view(), name='InvoiceProductsDelete'),
   path('PrintInvoice/<int:id>/', PrintInvoice, name='PrintInvoice'),
]