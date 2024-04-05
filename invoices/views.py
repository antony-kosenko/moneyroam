import logging
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Sum

from django_filters.views import FilterView
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, UpdateView

from invoices.models import Transaction
from invoices.services import TransactionServices, CategoryServices
from invoices.filters import TransactionsFilter, TransactionsListFilter
from invoices.forms import NewInvoiceForm, InvoiceUpdateForm


logger = logging.getLogger(__name__)

transaction_service = TransactionServices()
category_service = CategoryServices()
transaction_filter = TransactionsFilter()


def create_transaction_view(request):
    """ View to handle creation of new Transaction object. """
    # !!! Form for transaction creation (GET) initials in context processor to be available globally.
    if request.method == "POST":
        form = NewInvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            new_invoice = Transaction(**form.cleaned_data)      
            new_invoice.user = request.user
            new_invoice.save()
            # TODO Add success/error messages
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', "/"))


class DashboardView(ListView):
    """ View implements dashboard functionality. """
    logger.debug("DashboardView requested.")
    model = Transaction
    template_name = "invoices/dashboard.html"
    ordering = "-date_created"


    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset.select_related("category__parent")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        user = self.request.user

        # retrieving incomes/expenses summary for current month
        incomes_this_month = transaction_service.transactions_this_month(
            user=user,
            operation="incomes"
            )
        
        incomes_this_month_sum = incomes_this_month.aggregate(
            Sum("value")
            ).get("value__sum")

        expenses_this_month = transaction_service.transactions_this_month(
            user=user,
            operation="expenses"
            )       
        expenses_this_month_sum = expenses_this_month.aggregate(
            Sum("value")
            ).get("value__sum", 0)
        
        # retrieving incomes/expenses summary for previous month      
        incomes_previous_month_sum = transaction_service.transactions_previous_month(
            user=user,
            operation="incomes",
            sum=True
            )

        expenses_previous_month_sum = transaction_service.transactions_previous_month(
            user=user,
            operation="expenses",
            sum=True
            )

        # retrieving final balance
        balance = transaction_service.get_final_balance(
            user=self.request.user
            )

        # retrieving category stats
        category_expenses_stats = category_service.expenses_this_month(
            user=self.request.user
            )
        
        if category_expenses_stats is None :
            top_expense_category, less_expense_category = None, None
        elif category_expenses_stats.count() == 1:
            top_expense_category, less_expense_category = category_expenses_stats.first(), None
        else:
            top_expense_category = category_expenses_stats.first()
            less_expense_category = category_expenses_stats.last()

        # getting most expensive purchase this month
        most_expensive_purchase_this_month = (
            expenses_this_month
            .order_by("-value")
            .first()
        )

        # getting teh highest income
        highest_income_this_month = (
            incomes_this_month
            .order_by("-value")
            .first()
        )

        category_summary_stats = [
                {"stats_header": "Top spends this month", "stats": top_expense_category},
                {"stats_header": "Less spends this month", "stats": less_expense_category},
                {"stats_header": "Most expensive purchase", "stats": most_expensive_purchase_this_month},
                {"stats_header": "Highest income", "stats": highest_income_this_month}
            ]
        # filtering None value data
        category_summary_stats = [stats for stats in category_summary_stats if stats["stats"] is not None]

        # updating context with new variables
        data_to_context = {
            "this_month_incomes_total": incomes_this_month_sum,
            "this_month_expenses_total": expenses_this_month_sum,
            "last_month_incomes_total": incomes_previous_month_sum,
            "last_month_expenses_total": expenses_previous_month_sum,
            "categories_summary_stats": category_summary_stats,
            "balance_summary": balance
        }
        logger.debug(f"Context data providing along with DashboardView: {data_to_context}.")
        data.update(data_to_context)
        return data


class TransactionsListView(FilterView):
    """ Lists all transactions """
    logger.debug("DashboardView requested.")

    model = Transaction
    ordering = "-date_created"
    template_name = "invoices/transactions.html"
    context_object_name = "transactions"
    paginate_by = 20
    filterset_class = TransactionsListFilter

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return (queryset.filter(user=self.request.user)
                        .select_related("category__parent"))


class TransactionDeleteView(DeleteView):
    """ Deletes an existing instance. """
    model = Transaction
    template_name = 'invoices/transaction_confirm_delete.html'
    context_object_name = "transaction"

    def get_success_url(self):
        if 'HTTP_REFERER' in self.request.META:
            return self.request.META['HTTP_REFERER']


class TransactionUpdateView(UpdateView):
    """ Updates an existing model. """
    model = Transaction
    form_class = InvoiceUpdateForm
    context_object_name = "transaction"
    template_name = "invoices/transaction_update.html"

    def get_success_url(self):
        if 'HTTP_REFERER' in self.request.META:
            return self.request.META['HTTP_REFERER']