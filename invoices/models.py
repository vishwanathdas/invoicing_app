# invoices/models.py
from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=200)

    def __str__(self):
        return self.invoice_no

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='invoice_details', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.invoice.invoice_no} - {self.description}"
