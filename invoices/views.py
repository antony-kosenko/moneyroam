import logging
from typing import Any
from urllib import request
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from invoices.models import Invoice

logger = logging.getLogger(__name__)


# class TransactionListAndCreateView(CreateView):
#     # TODO Check later if i really need 2 in 1 view. 
#     """ Lists transactions depends on filter parameters passed (by default lists all transactions).
#     Handles creation of new transaction as well."""
#     model = Invoice
#     form_class = NewInvoiceForm
#     template_name = "invoices/dashboard.html"
#     success_url = reverse_lazy("invoices:transaction_list_and_create")
    
#     ALLOWED_TRANSACTION_TYPES = ("expenses", "incomes")
    
#     # using context data to pass a list of transactions 
#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         # retrieving 'type' parameter requested for invoice filtering
#         filter_type = self.request.GET.get("type")
#         logger.info(f"TransactionsListAndCreateView requested by {self.request.user.id}. "
#                     f"Filter parameter = {filter_type}")
#         # forming filtered queryset
#         if filter_type in self.ALLOWED_TRANSACTION_TYPES:
#             invoices_list = Invoice.objects.filter(operation=filter_type)            
#         else:
#             invoices_list = Invoice.objects.all()
#         # append a new data to context data
#         kwargs["invoice_list"] = invoices_list     
#         return super(TransactionListAndCreateView, self).get_context_data(**kwargs)

class CreateTransactionView(CreateView):
    """ Creates a new Transaction object."""
    
    model = Invoice
    template_name = "blank_page.html"
    fields = "__all__"
    
    def get_success_url(self) -> str:
        """ Returns a same page where the view calles from. """
        return self.request.META.get('HTTP_REFERER', "/")


class DashboardView(ListView):
    """ View implemets dashboard functionality. """
    
    template_name = "invoices/dashboard.html"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Invoice.objects.all()
    
    
    