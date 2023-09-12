from django.urls import path
from invoices.views import transactions_list_view

urlpatterns = [
    path("", transactions_list_view, name="transactions_list"),
]
