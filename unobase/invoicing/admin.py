'''
Created on 01 Mar 2013

@author: michael
'''
from django.contrib import admin
from unobase.invoicing import models

admin.site.register(models.InvoiceCompany)
admin.site.register(models.InvoiceBank)
admin.site.register(models.Invoice)
admin.site.register(models.InvoiceRecord)