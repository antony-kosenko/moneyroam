from datetime import datetime


class TransactionsFilter:
    """ Contains a filtering methods for Invoice model. """

    @classmethod
    def transaction_by_date_filter(
            cls,
            year: int | None = None,
            month: int | None = None,
            day: int | None = None
    ) -> dict:
        """ Returns a valid filter parameters to search transaction by date. """
        filter_parameters_requested = {"date_created__year": year, "date_created__month": month,
                                       "date_created__day": day}
        # removing parameters with None value
        not_none_parameters = cls._get_not_none_values(filter_parameters_requested)

        # checking if parameters provided then filter will be applied with these parameters.
        # Otherwise, returns the current year and month.
        if not_none_parameters:
            return not_none_parameters
        else:
            return {
                "date_created__year": datetime.today().year,
                "date_created__month": datetime.today().month,
            }

    @staticmethod
    def _get_not_none_values(iterable: dict) -> dict:
        """ Takes List or Dict as parameter and returns the same type of iterable filtering out None values. """
        # removing keys with values equal 'None'
        not_none_variables_list = {key: value for key, value in iterable.items() if value is not None}
        return not_none_variables_list
