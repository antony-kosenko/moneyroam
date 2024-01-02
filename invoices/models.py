from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from preferences.models import CURRENCY_CHOICE


OPERATION_TYPE = (
    ("incomes", "incomes"),
    ("expenses", "expenses")
)


def category_image_path(instance, filename):
    # uploading file to dynamic PATH
    return f"invoices/category/category_custom_img/{instance.name.lower()}/{filename}"


class Category(MPTTModel):
    """ Category model. 
    Represents a category where money have been spent/earned."""

    name = models.CharField(max_length=54, unique=True)
    image = models.ImageField(
        upload_to=category_image_path,
        default="invoices/category/default_category_img.svg",
        blank=True,
        null=True
    )
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True, max_length=54, blank=True)

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ('name',)
    
    class Meta:
        unique_together = ("name", "slug")
        verbose_name_plural = "Categories"


class Transaction(models.Model):
    """ Invoice model.
     Represents a basic income/outcome transaction. """
    
    title = models.CharField(max_length=32, verbose_name="Title")
    category = models.ForeignKey(Category, related_name="transactions", on_delete=models.CASCADE, null=True, blank=True)
    operation = models.CharField(max_length=8, choices=OPERATION_TYPE, verbose_name="operation")
    value = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="value")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE, verbose_name="currency")
    # TODO add image field for bill photo feature
    comment = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Transactions"
        ordering = ["-date_created"]

    def __str__(self):
        return f"[{self.date_created}] {self.title} [{self.operation}]"
        
    def __repr__(self) -> str:
        return f"{self.operation} | {self.title}"
        