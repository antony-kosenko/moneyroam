import logging
from typing import Any
import datetime

from django.views.generic import CreateView, ListView
from django.db.models import Sum

from invoices.models import Transaction
from invoices.services import TransactionServices
from invoices.forms import NewInvoiceForm

logger = logging.getLogger(__name__)

transaction_service = TransactionServices()


# class CreateTransactionView(CreateView):
#     """ Creates a new Transaction object."""
#     logger.debug("CreateTransactionView requested.")
    
#     model = Transaction
#     template_name = "blank_page.html"
#     fields = "__all__"
    
#     def get_success_url(self) -> str:
#         """ Returns a same page where the view calles from. """
#         logger.info("Invoice creation form submitted succesfully.")
#         return self.request.META.get('HTTP_REFERER', "/")

def create_transaction_view(request):
    if request.method == "POST":
        form = NewInvoiceForm(request.POST)
        if form.is_valid():
            new_invoice = Transaction(**form.cleaned_data)
            
            user_currency = request.user.config.currency
            
            # if user_currency != new_invoice.currency:
            #     match # TODO Continue here. Implement currency exchange
            
            

        


class DashboardView(ListView):
    """ View implemets dashboard functionality. """
    logger.debug("DashboardView requested.")
    model = Transaction
    template_name = "invoices/dashboard.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        
        # retrieving incomes/expenses summary for current month
        incomes_this_month = transaction_service.get_transaction_by_date(
            operation="income"
            ).aggregate(Sum("value"))
        expenses_this_month = transaction_service.get_transaction_by_date(
            operation="expense"
            ).aggregate(Sum("value"))
        
        # getting previous month data
        current_month_first_day = datetime.date.today().replace(day=1)
        last_month = current_month_first_day - datetime.timedelta(days=1)
        
        # retrieving incomes/expenses summary for previous month
        incomes_last_month = transaction_service.get_transaction_by_date(
            operation="income",
            month=last_month.month
            ).aggregate(Sum("value"))
        expenses_last_month = transaction_service.get_transaction_by_date(
            operation="expense",
            month=last_month.month
            ).aggregate(Sum("value"))
        
        # balance
        total_expenses = Transaction.objects.filter(operation="expense").aggregate(Sum("value"))
        total_incomes = Transaction.objects.filter(operation="income").aggregate(Sum("value"))
        try:
            balance_summary  = total_incomes["value__sum"] - total_expenses["value__sum"]
        except TypeError:
            balance_summary = 0
        
        # updating context with new variables
        data_to_context = {
            "this_month_incomes_total": incomes_this_month["value__sum"],
            "this_month_expenses_total": expenses_this_month["value__sum"],
            "last_month_incomes_total": incomes_last_month["value__sum"],
            "last_month_expenses_total": expenses_last_month["value__sum"],
            "balance_summary": balance_summary
        }
        
        logger.info(f"Context data providing along with DashboardView: {data_to_context}.")
        data.update(data_to_context)
        return data
    
    
class TransactionsListView(ListView):
    """ Lists all transactions """
    logger.debug("DashboardView requested.")
    
    model = Transaction
    template_name = "invoices/transactions.html"
    paginate_by = 7