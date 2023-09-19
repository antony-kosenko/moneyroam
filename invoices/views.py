from typing import Any, Dict
from django.urls import reverse_lazy,reverse

from django.views.generic.edit import CreateView

from invoices.models import Invoice
from invoices.forms import NewInvoiceForm


class TransactionListAndCreateView(CreateView):
    """ Lists transactions depends on filter parameters passed (by default lists all transactions).
    Handles creation of new transaction as well."""
    model = Invoice
    form_class = NewInvoiceForm
    template_name = "invoices/transactions.html"
    success_url = reverse_lazy("invoices:transaction_list_and_create")
    
    # using context data to pass a list of transactions
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        queryset = Invoice.objects.all()
        # retrieving 'type' parameter requested for invoice filtering
        filter_type = self.request.GET.get("type")
        # forming filtered queryset
        if filter_type == "outcome":
            queryset = queryset.filter(operation__startswith="-")
        elif filter_type == "income":
            queryset = queryset.exclude(operation__startswith="-")
        
        kwargs["invoice_list"] = queryset
    
        return super(TransactionListAndCreateView, self).get_context_data(**kwargs)
    