import logging
from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from invoices.models import Invoice

logger = logging.getLogger(__name__)


class CreateTransactionView(CreateView):
    """ Creates a new Transaction object."""
    logger.debug("CreateTransactionView requested.")
    
    model = Invoice
    template_name = "blank_page.html"
    fields = "__all__"
    
    def get_success_url(self) -> str:
        """ Returns a same page where the view calles from. """
        
        logger.info("Invoice creation form submitted succesfully.")
        return self.request.META.get('HTTP_REFERER', "/")


class DashboardView(ListView):
    """ View implemets dashboard functionality. """
    logger.debug("DashboardView requested.")
    
    template_name = "invoices/dashboard.html"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Invoice.objects.all()
    
    
    