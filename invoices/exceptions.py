from typing import Any, Mapping, Optional
from django.core.exceptions import ValidationError


class InvoiceDoesNotExist(ValidationError):
    def __init__(self, message: str = "Invoice with given data does't exist.", *args, **kwargs) -> None:
        super().__init__(message, *args, **kwargs)