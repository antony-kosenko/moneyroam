from typing import Any

from django.db.models import QuerySet

from core.interfaces import EnvoiceBaseInterface

from invoices.dto import PatchInvoiceDTO, InvoiceDTO, NewInvoiceDTO
from invoices.models import Invoice
from invoices.exceptions import InvoiceDoesNotExist

# TODO Check return values' type annotation

class InvoiceRepository(EnvoiceBaseInterface):
    """ Invoice interface.
     Performs manipulations with database's objects utilizing Django ORM. """
    
    def get_all_invoices(self) -> list[InvoiceDTO]:
        """ Retrieves all invoices' objects from database """
        invoices = Invoice.objects.select_related("category").all()
        return self._to_multiple_invoice_dto(invoices)
    
    def get_invoice_by_pk(self, invoice_pk: int | str) -> InvoiceDTO | None:
        """ Retrieves an invoice with provided Id if exists and returns None instead."""
        invoice = Invoice.objects.filter(pk=invoice_pk).first()
        if invoice is not None:
            return self._to_invoice_dto(invoice)
        else:
            raise InvoiceDoesNotExist()
    
    def create_invoice(self, new_invoice_dto: NewInvoiceDTO) -> InvoiceDTO:
        """ Creates new Invoice object in database."""
        new_invoice = Invoice.objects.create(
            title = new_invoice_dto.title,
            money_transaction = new_invoice_dto.money_transaction,
            currency = new_invoice_dto.currency,
            category = new_invoice_dto.category
        )
        return self._to_invoice_dto(new_invoice)
    
    def patch_invoice(self, invoice_pk: int | str, data_dto: PatchInvoiceDTO) -> InvoiceDTO:
        """ Edits invoice's object selected by given ID """
        invoice = Invoice.objects.filter(pk=invoice_pk).first()
        if invoice is not None:
            # updating selected invoice object with given not None values data:
            invoice_fields_updated = self._not_none_attributes_filter(invoice=invoice, dto_for_update=data_dto)
            invoice.save(update_fields=invoice_fields_updated)
            return self._to_invoice_dto(invoice=invoice)
        else:
            raise InvoiceDoesNotExist()

    def delete_invoice(self, invoice_pk: int | str) -> tuple | None:
        """ Deletes invoice object with given ID if exists. Returns True if success otherwise returns None"""
        invoice = Invoice.objects.filter(pk=invoice_pk).first()
        if invoice is not None:
            invoice.delete()

    def _to_invoice_dto(self, invoice: Invoice) -> InvoiceDTO:
        """ Converts django model's object(s) to DTO """
        dto = InvoiceDTO(
            pk = invoice.pk,
            title = invoice.title,
            money_transaction = invoice.money_transaction,
            currency = invoice.currency,
            date_created = invoice.date_created,
            category = invoice.category
        )
        return dto

    def _to_multiple_invoice_dto(self, invoices: QuerySet[Invoice]) -> list[InvoiceDTO]:
        """ Converts multiple django models to DTO """
        invoices_dto = map(self._to_invoice_dto, invoices)
        return list(invoices_dto)
    
    def _not_none_attributes_filter(self, invoice: Invoice, dto_for_update: PatchInvoiceDTO) -> list | None:
        """ Filters incoming DTO for not None values and use them to update existing Invoice objects."""
        dto_to_dict = dict(dto_for_update)
        not_none_attributes = {key: value for key, value in dto_to_dict.items() if value is not None}
        for attr, value in not_none_attributes.items():
            setattr(invoice, attr, value)
        return not_none_attributes.keys() if not_none_attributes else None
