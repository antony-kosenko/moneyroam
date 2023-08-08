from django.contrib import admin

from invoices.models import Invoice, Category


admin.site.register(Invoice)
admin.site.register(Category)