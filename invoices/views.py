from django.shortcuts import render

from invoices.repositories import InvoiceRepository
from invoices.dto import NewInvoiceDTO

def test_view(request):
    repository = InvoiceRepository()
    get_invoice = repository.get_invoice_by_pk(1)
    context_data = {
            "data": get_invoice
        }
    print(context_data["data"])

    return render(request, template_name="homescreen_base.html", context=context_data)