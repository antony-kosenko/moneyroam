import datetime


def current_date_context(request):
    """ Contains a form for new transaction creation """
    return {"current_date": datetime.date.today()}
