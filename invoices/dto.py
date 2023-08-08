from datetime import datetime
from pydantic import BaseModel


class CategoryDTO(BaseModel):
    name: str
    parent: "CategoryDTO"
    slug: str | None = None


class InvoiceDTO(BaseModel):
    pk: int | str
    title: str
    money_transaction: float
    currency: str
    date_created: datetime | None
    category: CategoryDTO | None = None


class NewInvoiceDTO(BaseModel):
    title: str
    money_transaction: float
    currency: str
    category: CategoryDTO | None


class PatchInvoiceDTO(BaseModel):
    title: str | None
    money_transaction: float | None
    category: CategoryDTO | None
    