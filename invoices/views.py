from django.shortcuts import render


def dashboard_view(request):
    return render(request, template_name="invoices/dashboard.html")


def transactions_list_view(request):
    """ Lists all transactions (paginated). """
    return render(request, template_name="invoices/transactions.html")
