from django.db.models import Sum, Count, query
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import *
import weasyprint
from .models import *
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.http import HttpResponse
from Core.models import *

# Create your views here.


class InvoiceList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = Invoice
    paginate_by = 12

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context


class InvoiceTrashList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = Invoice
    paginate_by = 12

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'trash'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context


class InvoiceCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'فاتورة مبيعات'
        context['message'] = 'create'
        context['action_url'] = reverse_lazy('Invoices:InvoiceCreate')
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=self.form_class)
        form.fields['seller'].queryset = ProductSellers.objects.filter(deleted=False)
        return form

    def form_valid(self, form):
        form.save()
        obj = form.save(commit=False)
        myform = Invoice.objects.get(id=obj.id)
        myform.creator = self.request.user
        myform.invoice_type = 1
        myform.save()
        return redirect('Invoices:InvoiceDetail', pk=myform.id)

    def get_success_url(self, **kwargs):
        messages.success(self.request, "تم اضافة فاتورة مبيعات بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.object.id})


class InvoiceUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل فاتورة مبيعات: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Invoices:InvoiceUpdate', kwargs={'pk': self.object.id})
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=self.form_class)
        form.fields['seller'].queryset = ProductSellers.objects.filter(deleted=False)
        return form

    def get_success_url(self, **kwargs):
        messages.success(self.request, "تم تعديل فاتورة مبيعات بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceList')


class InvoiceSave(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceSaveForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حفظ فاتورة مبيعات: ' + str(self.object)
        context['message'] = 'inv_save'
        context['action_url'] = reverse_lazy('Invoices:InvoiceSave', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self, **kwargs):
        messages.success(self.request, "تم حفظ الفاتورة بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        total = form.cleaned_data.get("total")
        discount = form.cleaned_data.get("discount")
        inv = form.save(commit=False)
        inv.overall = float(total) - float(discount)
        form.save()
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.saved = 1
        myform.save()
        return redirect(self.get_success_url())


class InvoiceBack(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceBackForm
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الغاء حفظ فاتورة مبيعات: ' + str(self.object)
        context['message'] = 'inv_back'
        context['action_url'] = reverse_lazy('Invoices:InvoiceBack', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        form.save()
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.saved = 0
        # myform.discount = 0.0
        myform.overall = 0.0
        myform.save()
        return redirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        messages.success(self.request, "تم الغاء حفظ الفاتورة بنجاح", extra_tags="success")
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.object.id})


class InvoiceDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Invoices:InvoiceList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف فاتورة مبيعات: ' + str(self.object)
        context['message'] = 'deletee'
        context['action_url'] = reverse_lazy('Invoices:InvoiceDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف فاتورة مبيعات " + str(self.object) + ' بنجاح ', extra_tags="danger")
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())


class InvoiceRestore(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Invoices:InvoiceTrashList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع فاتورة مبيعات: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Invoices:InvoiceRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم استرجاع فاتورة مبيعات " + str(self.object) + ' بنجاح ', extra_tags="dark")
        myform = Invoice.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())


class InvoiceSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Invoice
    form_class = InvoiceDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Invoices:InvoiceTrashList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف فاتورة مبيعات : ' + str(self.object.id) + 'بشكل نهائي'
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Invoices:InvoiceSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم حذف فاتورة مبيعات " + str(self.object.id) + " نهائيا بنجاح ", extra_tags="success")
        my_form = Invoice.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())


def InvoiceDetail(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    product = InvoiceItem.objects.filter(invoice=invoice).order_by('id')
    count_product = product.count()

    total = product.aggregate(total=Sum('total_price')).get('total')
    quantity = product.aggregate(quantity=Sum('quantity')).get('quantity')

    if total:
        invoice.total = total
        invoice.save()

    form = InvoiceProductsForm()
    products = []
    for prod in product:
        products.append(prod.item.id)

    form.fields['item'].queryset = Product.objects.filter(deleted=False).exclude(id__in=products)

    type_page = "list"
    page = "active"
    action_url = reverse_lazy('Invoices:AddProductInvoice', kwargs={'pk': invoice.id})

    context = {
        'invoice': invoice,
        'type': type_page,
        'page': page,
        'form': form,
        'action_url': action_url,
        'product': product,
        'count_product': count_product,
        'total': total,
        'qu': quantity,
        'date': datetime.now().date(),

    }
    return render(request, 'Invoices/invoice_detail.html', context)


def AddProductInvoice(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    product = InvoiceItem.objects.filter(invoice=invoice).order_by('id')
    count_product = product.count()

    form = InvoiceProductsForm(request.POST or None)
    formm = InvoiceProductsForm()

    type_page = "list"
    page = "active"
    action_url = reverse_lazy('Invoices:AddProductInvoice', kwargs={'pk': invoice.id})

    context = {
        'invoice': invoice,
        'type': type_page,
        'page': page,
        'form': formm,
        'action_url': action_url,
        'product': product,
        'count_product': count_product
    }

    if form.is_valid():
        quantity = form.cleaned_data.get("quantity")
        item = form.cleaned_data.get("item")
        trans = item.quantity

        if trans >= quantity:
            obj = form.save(commit=False)
            obj.invoice = invoice
            obj.save()
            messages.success(request, " تم اضافة منتج الي الفاتورة بنجاح ", extra_tags="success")
        else:
            messages.success(request, " لاتوجد كمية كافية من المنتج داخل المخزن ", extra_tags="danger")
        return redirect('Invoices:InvoiceDetail', pk=invoice.id)

    return render(request, 'Invoices/invoice_detail.html', context)


class InvoiceProductsUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = InvoiceItem
    form_class = InvoiceProductsFormUpdate
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل المنتج: ' + str(self.object.item)
        context['message'] = 'updatee'
        context['inv_update'] = 'update'
        context['action_url'] = reverse_lazy('Invoices:InvoiceProductsUpdate', kwargs={'pk': self.object.id, 'id': self.object.invoice.id})
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class=self.form_class)
        form.fields['item'].queryset = Product.objects.filter(id=self.object.item.id)
        return form

    def get_success_url(self, **kwargs):
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.kwargs['id']})

    def form_valid(self, form):
        quantity = form.cleaned_data.get("quantity")
        unit_price = form.cleaned_data.get("unit_price")
        item = form.cleaned_data.get("item")
        trans = item.quantity
        object_item = self.object.item

        if trans >= quantity:
            prod = form.save(commit=False)
            prod.total_price = float(quantity) * float(unit_price)
            form.save()
            messages.success(self.request, " تم تعديل منتج " + str(object_item) + " بنجاح ", extra_tags="success")
        else:
            messages.success(self.request, " لاتوجد كمية كافية من المنتج داخل المخزن ", extra_tags="danger")
        return redirect(self.get_success_url())


class InvoiceProductsDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = InvoiceItem
    form_class = InvoiceProductsDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Invoices:InvoiceDetail', kwargs={'pk': self.kwargs['id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف المنتج: ' + str(self.object.item)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Invoices:InvoiceProductsDelete', kwargs={'pk': self.object.id, 'id': self.object.invoice.id})
        return context

    def form_valid(self, form):
        object_item = self.object.item
        messages.success(self.request, " تم حذف المنتج " + str(object_item) + " من الفاتورة بنجاح ", extra_tags="success")
        my_form = InvoiceItem.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())


def PrintInvoice(request, id):
    date = datetime.now()
    invoice = Invoice.objects.get(id=id)
    invoice_items = InvoiceItem.objects.filter(invoice=invoice, deleted=0)
    shop_setting = SystemInformation.objects.all()
    if shop_setting.count() > 0:
        shop_setting = shop_setting.last()
    else:
        shop_setting = None
    context = {
        'date': date,
        'user': request.user.username,
        'invoice': invoice,
        'invoice_items': invoice_items,
        'shop_setting': shop_setting,
    }
    html_string = render_to_string('Invoices/print_main_invoice.html', context)
    html = weasyprint.HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf(stylesheets=[weasyprint.CSS('static/assets/css/main_invoice_pdf.css')], presentational_hints=True)
    response = HttpResponse(pdf, content_type='application/pdf')
    return response
