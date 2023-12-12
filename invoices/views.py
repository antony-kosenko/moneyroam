import logging
from typing import Any
import datetime

from django.db.models.functions import Cast
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.db.models import Sum, Q, FloatField, ExpressionWrapper, IntegerField

from invoices.models import Transaction, Category
from invoices.services import TransactionServices
from invoices.forms import NewInvoiceForm

from utils.currency_manager import CurrencyExchangeManager

logger = logging.getLogger(__name__)

transaction_service = TransactionServices()


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
        incomes_this_month = (transaction_service.get_transaction_by_date(operation="income")
                              .aggregate(Sum("value")).get("value__sum"))
        expenses_this_month = (transaction_service.get_transaction_by_date(operation="expense")
                               .aggregate(Sum("value")).get("value__sum"))
        # getting previous month data
        current_month_first_day = datetime.date.today().replace(day=1)
        last_month = current_month_first_day - datetime.timedelta(days=1)

        # retrieving incomes/expenses summary for previous month
        incomes_last_month = transaction_service.get_transaction_by_date(
            operation="income",
            month=last_month.month
        ).aggregate(Sum("value")).get("value__sum")
        expenses_last_month = transaction_service.get_transaction_by_date(
            operation="expense",
            month=last_month.month
        ).aggregate(Sum("value")).get("value__sum")

        # balance calculation
        total_expenses = Transaction.objects.filter(operation="expense").aggregate(Sum("value")).get("value__sum")
        total_incomes = Transaction.objects.filter(operation="income").aggregate(Sum("value")).get("value__sum")
        try:
            balance_summary = total_incomes - total_expenses
        except TypeError:
            if (total_incomes is None) and (total_expenses is None):
                balance_summary = 0
            elif total_incomes is None:
                balance_summary = -total_expenses
            elif total_expenses is None:
                balance_summary = total_incomes
            else:
                balance_summary = 0

        # categories expenses sum stats wrapped with annotation
        expenses_category_this_month = (
            Category.objects.filter(transactions__operation="expense")
            .annotate(
                expenses_sum=Sum('transactions__value', filter=Q(
                    transactions__date_created__month=datetime.date.today().month) & Q(
                    transactions__date_created__year=datetime.date.today().year)),
            )
            # TODO escape zero division error
            .annotate(
                percentage=ExpressionWrapper(
                    Cast('expenses_sum', output_field=FloatField()) / float(expenses_this_month) * 100,
                    output_field=IntegerField())
            )
            .order_by('-percentage')
        )
        top_expense_category = expenses_category_this_month.first()
        less_expense_category = expenses_category_this_month.last()
        most_expensive_purchase = (Transaction.objects.filter(
            operation="expense",
            date_created__month=datetime.date.today().month,
            date_created__year=datetime.date.today().year
        )
                                   .order_by("-value")
                                   .first()
                                   )
        highest_income = (Transaction.objects.filter(
            operation="income",
            date_created__month=datetime.date.today().month,
            date_created__year=datetime.date.today().year
        )
                                    .order_by("-value")
                                    .first()
                          )
        # updating context with new variables
        data_to_context = {
            "this_month_incomes_total": incomes_this_month,
            "this_month_expenses_total": expenses_this_month,
            "last_month_incomes_total": incomes_last_month,
            "last_month_expenses_total": expenses_last_month,
            "top_expenses_category_this_month": top_expense_category,
            "less_expenses_category_this_month": less_expense_category,
            "most_expensive_transaction": most_expensive_purchase,
            "highest_income_transaction": highest_income,
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

    def get_queryset(self):
        if self.request.GET.get("transaction") == "income":
            qs = super().get_queryset().filter(operation="income")
        elif self.request.GET.get("transaction") == "expense":
            qs = super().get_queryset().filter(operation="expense")
        else:
            qs = super().get_queryset()
        return qs
