from invoices.forms import NewInvoiceForm

def create_transaction_form(request):
    """ Contains a form for new transaction creation """
    return {"form": NewInvoiceForm()}