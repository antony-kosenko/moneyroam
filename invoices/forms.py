from django import forms
from django.utils.translation import gettext_lazy as _

from invoices.models import Transaction


class NewInvoiceForm(forms.ModelForm):
    
    class Meta:
        model = Transaction
        fields = ("title", "category", "operation", "value", "currency")
        help_texts = {
            "operation": _("Money spent/recieved. For expenses use a negative value.")
        }