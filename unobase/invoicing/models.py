'''
Created on 01 Mar 2013

@author: michael
'''
from decimal import Decimal

from django.db import models

from photologue.models import ImageModel
from unobase.invoicing import constants

class InvoiceCompany(models.Model):
    name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    address_line_3 = models.CharField(max_length=255, blank=True, null=True)
    vat_number = models.CharField(max_length=10, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.name
    
class InvoiceBank(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    branch_code = models.CharField(max_length=6)
    swift_code = models.CharField(max_length=8, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.name

class Invoice(ImageModel):
    from_company = models.ForeignKey(InvoiceCompany, related_name='from_invoices')
    to_company = models.ForeignKey(InvoiceCompany, related_name='to_invoices')
    
    number = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    po_number = models.CharField(max_length=9, blank=True, null=True)
    vat_percentage = models.PositiveSmallIntegerField(default=14)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal(0.0))
    
    account_type = models.CharField(max_length=50, 
                                    choices=constants.ACCOUNT_TYPE_CHOICES, 
                                    default=constants.ACCOUNT_TYPE_CHEQUE,
                                    blank=True, null=True)
    account_number = models.CharField(max_length=10, blank=True, null=True)
    
    bank = models.ForeignKey(InvoiceBank, related_name='invoices')
    
    @property
    def vat_amount(self):
        if self.vat_percentage > 0:
            return self.sub_total_amount * Decimal(self.vat_percentage / 100.0)
        
        return 0.0
    
    @property
    def sub_total_amount(self):
        total_amount = 0
        
        for record in self.records.all():
            total_amount += record.total_amount
            
        return (total_amount * 100) / (self.vat_percentage + 100)
        
    @property
    def total_amount(self):
        return self.sub_total_amount + self.vat_amount
    
    def save(self, *args, **kwargs):
        self.number = Invoice.objects.count() + 1
        
        super(Invoice, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return u'%i' % self.number
    
    
class InvoiceRecord(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='records')
    order = models.PositiveSmallIntegerField(default=0)
    description = models.CharField(max_length=255, default='')
    quantity = models.PositiveIntegerField(default=1)
    currency = models.CharField(max_length=3, default='ZAR')
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    
    @property
    def total_amount(self):
        return self.amount * self.quantity
    
    class Meta:
        ordering = ['order']