from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


CURRENCY_CHOICE = (
    ("UAH", "₴"),
    ("USD", "$"),
    ("EUR", "€")
)

OPERATION_TYPE = (
    ("income", "income"),
    ("expense", "expense")
)


class Category(MPTTModel):
    """ Category model. 
    Represents a category where money have been spent/earned."""

    name = models.CharField(max_length=54, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True, max_length=54, blank=True)

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ('name',)
    
    class Meta:
        verbose_name_plural = "Categories"


class Invoice(models.Model):
    """ Invoice model.
     Represents a basic income/outcome transaction. """
    
    title = models.CharField(max_length=32, verbose_name="Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    operation = models.CharField(max_length=7, choices=OPERATION_TYPE, verbose_name="operation")
    value = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="money_value")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE, verbose_name="currency")
    # TODO add image field for bill photo feature
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ("-date_created",)
        verbose_name_plural = "Invoices"
        ordering = ["-date_created"]

    def __str__(self):
        return f"[{self.date_created}] {self.title} [{self.operation}]"
        
    def __repr__(self) -> str:
        return f"{self.operation} | {self.title}"
        