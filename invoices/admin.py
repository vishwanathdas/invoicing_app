from django.contrib import admin
from .models import Invoice,InvoiceDetail
# Register your models here.

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display=['date','invoice_no','customer_name',]
    


@admin.register(InvoiceDetail)
class InvoicedetailsAdmin(admin.ModelAdmin):
    list_display=['invoice','description','quantity','unit_price','price']