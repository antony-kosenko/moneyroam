from django import forms
from django.utils.translation import gettext_lazy as _

from invoices.models import Invoice


class NewInvoiceForm(forms.ModelForm):
    
    class Meta:
        model = Invoice
        fields = ("title", "category", "operation", "currency")
        help_texts = {
            "operation": _("Money spent/recieved. For expenses use a negative value.")
        }