import logging
import datetime

from django.db.models import Q, Sum, ExpressionWrapper, FloatField, F
from django.db.models.functions import Round

from accounts.models import CustomUser

from invoices.models import Transaction, Category
from invoices.filters import TransactionsFilter

logger = logging.getLogger(__name__)

transaction_filter = TransactionsFilter()


class TransactionServices:
    """ Implements Transaction model services. """
    __ALLOWED_OPERATIONS = ["expenses", "incomes"]

    def get_all_transactions(self, user: CustomUser, operation: str | None = None, summary: bool = False):
        """ Returns Transaction object queryset."""

        logger.debug(f"Method 'get_transaction_by_date' requested with parameters: "
                     f"{operation:}.")

        # checking if given parameter is allowed. Rising an exception otherwise.
        if operation not in self.__ALLOWED_OPERATIONS:
            logger.exception(f"ValueError risen. Invalid type '{operation}'. "
                             f"Allowed types: {self.__ALLOWED_OPERATIONS}.")
            raise ValueError(f"Invalid operation type '{operation}'. Allowed types: {self.__ALLOWED_OPERATIONS}.")
        
        queryset = Transaction.objects.filter(user=user)

        if operation:
            queryset = Transaction.objects.filter(user=user, operation=operation)

        if summary:
            return queryset.aggregate(Sum("value")).get("value__sum")
        else:
            return queryset

    def transactions_this_month(self, user: CustomUser, operation: str | None = None, summary: bool = False):
        """ Retrieves all transactions for this month unless operation specified.
         If 'summary' equals True returns sum of all 'value' fields for all transactions returned. """
        
        transactions = (
            self.get_all_transactions(user=user, operation=operation)
            .filter(transaction_filter.transaction_date_filter(month="current"))
        )

        if not transactions:
            return 0
        
        if summary:
            return transactions.aggregate(Sum("value")).get("value__sum")
        else:
            return transactions

    def transactions_previous_month(self, user: CustomUser, operation: str | None = None, summary: bool = False):
        """ Retrieves all transactions for previous month unless operation specified.
         If 'summary' equals True returns sum of all 'value' fields for all transactions returned. """

        transactions = (
            self.get_all_transactions(user=user, operation=operation)
            .filter(transaction_filter.transaction_date_filter(month="previous"))
        )

        if not transactions :
            return 0

        if summary:
            return transactions.aggregate(Sum("value")).get("value__sum")
        else:
            return transactions

    def get_final_balance(self, user: CustomUser) -> int:
        """ Calculates final balance. """
        # getting summary of expenses and incomes
        total_expenses = self.get_all_transactions(user=user, operation="expenses", summary=True)
        total_incomes = self.get_all_transactions(user=user, operation="incomes", summary=True)

        try:
            balance_summary = total_incomes - total_expenses
        except TypeError:
            if total_incomes is None and total_expenses is not None:
                balance_summary = -total_expenses
            elif total_expenses is None and total_incomes is not None:
                balance_summary = total_incomes
            else:
                balance_summary = 0

        return balance_summary


transaction_service = TransactionServices()


class CategoryServices:
    """ Implements Category model services. """

    @staticmethod
    def expenses_in_categories_this_month(user: CustomUser):
        """ Categories expenses sum stats for current month wrapped with annotation. """

        expenses_this_month_sum = transaction_service.transactions_this_month(
            user=user,
            operation="expenses",
            summary=True
            )
        
        if expenses_this_month_sum > 0 :
            # calculating category stats with annotated 'expenses_sum' (calculates spends sum in every category) and
            # 'percentage' (calculates spends in category as percentage of total spends in current month)

            expenses_category_this_month = (
                Category.objects.filter(
                    Q(transactions__date_created__month=datetime.date.today().month) & Q(
                        transactions__date_created__year=datetime.date.today().year),
                        transactions__user=user,
                        transactions__operation="expenses")
                .annotate(
                    expenses_sum=Sum('transactions__value')
                )
                # TODO is there a better way to avoid 'zero devision'?
                .annotate(
                    percentage=Round(ExpressionWrapper((F('expenses_sum') / expenses_this_month_sum * 100), output_field=FloatField()), 2))
                .order_by('-percentage')
            )

            print("first", expenses_category_this_month)
            return expenses_category_this_month
        else:
            return None

