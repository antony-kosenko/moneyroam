from abc import ABC, abstractmethod

from invoices.dto import InvoiceDTO, NewInvoiceDTO, PatchInvoiceDTO

# TODO Edit with actual needs. If DTO not being used then replace type annotation for return values
class EnvoiceBaseInterface(ABC):
    """ Invoice base abstract interface. """

    @abstractmethod
    def get_all_invoices(self) -> list[InvoiceDTO]:
        pass
    
    @abstractmethod
    def get_invoice_by_pk(self, invoice_pk: int | str) -> InvoiceDTO:
        pass

    @abstractmethod
    def create_invoice(self, new_invoice_dto: NewInvoiceDTO) -> InvoiceDTO:
        pass

    @abstractmethod
    def patch_invoice(self, data_dto: PatchInvoiceDTO) -> InvoiceDTO:
        pass

    @abstractmethod
    def delete_invoice(self, invoice_pk: int | str) -> bool | None:
        pass
