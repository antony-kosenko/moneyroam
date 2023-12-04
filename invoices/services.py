import logging
from django.db.models import Q

from invoices.models import Transaction
from invoices.filters import TransactionsFilter

logger = logging.getLogger(__name__)


class TransactionServices:
    
    __ALLOWED_TRANSACTIONS = ["expense", "income"]

    def get_transaction_by_date(
        self, 
        operation: str | None = None,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None
        ):
        
        """ Returns Transaction object queryset for a given date.
        By default date is a current date. """
        logger.debug(f"Method 'get_transaction_by_date' requested with parameters:\
                     operation = {operation},\
                     year = {year},\
                     month = {month},\
                     day = {day}.")
        # checking if given parameter is allowed. Rising an exception otherwise.
        if operation not in self.__ALLOWED_TRANSACTIONS:
            logger.exception(f"ValueError risen. Invalid type '{operation}'. Allowed types: {self.__ALLOWED_TRANSACTIONS}.")
            raise ValueError(f"Invalid operation type '{operation}'. Allowed types: {self.__ALLOWED_TRANSACTIONS}.")
        # applying a filter class method to get a parameters for further filtering
        transaction_by_date_filter_parameters = TransactionsFilter.transaction_by_date_filter(
            year=year,
            month=month,
            day=day
        )

        queryset = Transaction.objects.filter(operation=operation).filter(Q(**transaction_by_date_filter_parameters))
        return queryset
        