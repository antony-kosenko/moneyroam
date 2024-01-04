import logging
from typing import Any

import django_filters.views
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from invoices.models import Transaction
from invoices.services import TransactionServices, CategoryServices
from invoices.filters import TransactionsFilter, TransactionsListFilter
from invoices.forms import NewInvoiceForm

from utils.currency_manager import CurrencyExchangeManager

logger = logging.getLogger(__name__)

transaction_service = TransactionServices()
category_service = CategoryServices()
transaction_filter = TransactionsFilter()


def create_transaction_view(request):
    if request.method == "POST":
        form = NewInvoiceForm(request.POST)
        if form.is_valid():
            new_invoice = Transaction(**form.cleaned_data)
            # retrieving user's currency preference for further converting if income is different from base currency
            user_currency = request.user.config.currency
            # performing currency conversion to maintain consistent data for statistic and analyse
            if user_currency != new_invoice.currency:
                transaction_converted_value = CurrencyExchangeManager.currency_converter(
                    value=new_invoice.value,
                    exchange_to=user_currency,
                    base=new_invoice.currency
                )
                new_invoice.value = transaction_converted_value
                new_invoice.currency = user_currency
            new_invoice.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', "/"))


class DashboardView(ListView):
    """ View implements dashboard functionality. """
    logger.debug("DashboardView requested.")
    model = Transaction
    template_name = "invoices/dashboard.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)

        # retrieving incomes/expenses summary for current month
        incomes_this_month = transaction_service.transactions_this_month("incomes", summary=True)
        expenses_this_month = transaction_service.transactions_this_month("expenses", summary=True)

        # retrieving incomes/expenses summary for previous month
        incomes_previous_month = transaction_service.transactions_previous_month(operation="incomes", summary=True)
        expenses_previous_month = transaction_service.transactions_previous_month(operation="expenses", summary=True)

        # retrieving final balance
        balance = transaction_service.get_final_balance()

        # retrieving category stats
        category_expenses_stats = category_service.expenses_in_categories_this_month()
        top_expense_category = category_expenses_stats.first()
        less_expense_category = category_expenses_stats.last()

        # getting most expensive purchase this month
        most_expensive_purchase_this_month = (
            transaction_service.get_all_transactions(operation="expenses")
            .filter(transaction_filter.transaction_date_filter(month="current"))
            .order_by("-value")
            .first()
        )
        highest_income_this_month = (
            transaction_service.get_all_transactions(operation="incomes")
            .filter(transaction_filter.transaction_date_filter(month="current"))
            .order_by("-value")
            .first()
        )
        # updating context with new variables
        data_to_context = {
            "this_month_incomes_total": incomes_this_month,
            "this_month_expenses_total": expenses_this_month,
            "last_month_incomes_total": incomes_previous_month,
            "last_month_expenses_total": expenses_previous_month,
            "categories_summary_stats": [
                {"stats_header": "Top expends this month", "stats": top_expense_category},
                {"stats_header": "Less spends this month", "stats": less_expense_category},
                {"stats_header": "Most expensive purchase", "stats": most_expensive_purchase_this_month},
                {"stats_header": "Highest income", "stats": highest_income_this_month}
            ],
            # "top_expenses_category_this_month": top_expense_category,
            # "less_expenses_category_this_month": less_expense_category,
            # "most_expensive_transaction": most_expensive_purchase_this_month,
            # "highest_income_transaction": highest_income_this_month,
            "balance_summary": balance
        }
        logger.info(f"Context data providing along with DashboardView: {data_to_context}.")
        data.update(data_to_context)
        return data


class TransactionsListView(django_filters.views.FilterView):
    """ Lists all transactions """
    logger.debug("DashboardView requested.")

    model = Transaction
    template_name = "invoices/transactions.html"
    context_object_name = "transactions"
    paginate_by = 7
    filterset_class = TransactionsListFilter

    def get_queryset(self):
        if self.request.GET.get("transaction") == "incomes":
            qs = super().get_queryset().filter(operation="incomes")
        elif self.request.GET.get("transaction") == "expenses":
            qs = super().get_queryset().filter(operation="expenses")
        else:
            qs = super().get_queryset()
        return qs
