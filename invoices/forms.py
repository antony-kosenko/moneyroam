from django import forms
from django.utils.translation import gettext_lazy as _
from mptt.forms import TreeNodeChoiceField

from invoices.models import Transaction, Category


class NewInvoiceForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Transaction
        fields = ("title", "category", "operation", "value", "currency")
        help_texts = {
            "operation": _("Money spent/received. For expenses use a negative value.")
        }
