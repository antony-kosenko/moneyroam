import datetime
from django.db.models import Q

import django_filters

from invoices.models import Transaction
from moneyroam.utils import clear_none_values


class TransactionsFilter:
    """ Contains a filtering methods for Invoice model. """

    def transaction_date_filter(
            self,
            year: int | None = None,
            month: int | str | None = None,
            day: int | None = None
    ) -> Q:
        """ Returns a valid filter parameters (unpacked) to search transaction by date.
        Allowed values in 'int' format. For month allowed 'str' values : 'current' and 'previous' which returns
        date current month/year and previous month/year respectively."""

        # Setting valid 'month' parameters for 'str' type
        __ALLOWED_MONTH_VALUES = ("current", "previous")
        if isinstance(month, str) and month in __ALLOWED_MONTH_VALUES:
            match month:
                case "current":
                    return Q(
                        date_purchased__year=datetime.datetime.today().year,
                        date_purchased__month=datetime.datetime.today().month
                    )
                case "previous":
                    return Q(**self._previous_month())
                case _:
                    raise ValueError(f"Not valid value provided for month. Valid values are: {__ALLOWED_MONTH_VALUES}")
        else:
            filter_parameters_requested = {"date_purchased__year": year,
                                           "date_purchased__month": month,
                                           "date_purchased__day": day
                                           }

            # removing parameters with None value
            not_none_parameters = clear_none_values(filter_parameters_requested)

            # checking if parameters provided then filter will be applied with these parameters.
            date_requested = {f"date_purchased__{k}": v for k, v in not_none_parameters.items()}
            return Q(**date_requested)

    @staticmethod
    def _previous_month():
        """ Returns previous month as date. """
        # getting previous month data
        current_month_first_day = datetime.datetime.today().replace(day=1)
        previous_month = current_month_first_day - datetime.timedelta(days=1)
        return {
            "date_purchased__month": previous_month.month,
            "date_purchased__year": previous_month.year
            }


class TransactionsListFilter(django_filters.FilterSet):
    """ Filters for Transaction list. """

    title = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Transaction title"
        )
    date_purchased = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Transaction
        fields = ["title", "category", "operation", "date_purchased"]
