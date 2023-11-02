from django.urls import path
from invoices.views import TransactionListAndCreateView

app_name = "invoices"

urlpatterns = [
    path("transactions/", TransactionListAndCreateView.as_view(), name="transaction_list_and_create"),
]
