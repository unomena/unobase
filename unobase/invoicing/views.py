'''
Created on 01 Mar 2013

@author: michael
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django_xhtml2pdf.utils import render_to_pdf_response

from unobase.invoicing import models

def download_invoice(request, pk):
    resp = HttpResponse(content_type='application/pdf')
    
    invoice = models.Invoice.objects.get(pk=pk)
    
    context_data = {
        'company_address_details': {'company_name': invoice.from_company.name,
                                    'address_line_1': invoice.from_company.address_line_1,
                                    'address_line_2': invoice.from_company.address_line_2,
                                    'address_line_3': invoice.from_company.address_line_3,
                                    'vat_number': invoice.from_company.vat_number
                                    },
        'customer_address_details': {'company_name': invoice.to_company.name,
                                    'address_line_1': invoice.to_company.address_line_1,
                                    'address_line_2': invoice.to_company.address_line_2,
                                    'address_line_3': invoice.to_company.address_line_3,
                                    'vat_number': invoice.to_company.vat_number
                                    },
        'invoice_details': {'invoice_number': invoice.number,
                            'invoice_date': invoice.date,
                            'po_number': invoice.po_number,
                            'vat_percentage': invoice.vat_percentage,
                            'total_amount': invoice.total_amount,
                            'total_amount_due': invoice.total_amount - invoice.amount_paid,
                            'sub_total_amount': invoice.sub_total_amount,
                            'vat_amount': invoice.vat_amount,
                            'amount_paid': invoice.amount_paid
                            },
        'banking_details': {
                            'account_type': invoice.get_account_type_display(),
                            'account_number': invoice.account_number,
                            'bank_name': invoice.bank.name,
                            'bank_branch': invoice.bank.branch,
                            'bank_branch_code': invoice.bank.branch_code,
                            'swift_code': invoice.bank.swift_code,
                            'vat_number': invoice.from_company.vat_number
                            },
        'columns': {'rows': invoice.records.all()}
    }
    
    #return render_to_response('sav/dashboard/invoice.html', context_data, context_instance=RequestContext(request))
    return render_to_pdf_response('invoicing/invoice.html', context_data)
