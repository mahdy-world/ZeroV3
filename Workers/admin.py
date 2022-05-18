from django.contrib import admin

from Workers.models import Worker, WorkerPayment, WorkerProduction

# Register your models here.
admin.site.register(Worker)
admin.site.register(WorkerPayment)
admin.site.register(WorkerProduction)