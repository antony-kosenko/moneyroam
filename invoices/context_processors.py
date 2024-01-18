from invoices.forms import NewInvoiceForm


def create_transaction_form(request):
    """ Contains a form for new transaction creation """
    user_currency = request.user.config.currency
    return {"transaction_creation_form": NewInvoiceForm(initial={'currency': user_currency})}
