from django.db import models

from common.models import BaseModel


class Deals(BaseModel):
    customer = models.CharField(max_length=255, null=False, blank=False, verbose_name="Customer")
    item = models.CharField(max_length=155, null=False, blank=False, verbose_name="Item")
    total = models.PositiveIntegerField(null=False, blank=False, verbose_name="Total")
    quantity = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name="Quantity")
    date = models.DateTimeField(null=False, blank=False, verbose_name="Date")

    def __str__(self) -> str:
        return f"{self.customer}: {self.item}"

    class Meta:
        db_table = "deals__deals"
        verbose_name = "Deal"
        verbose_name_plural = "Deals"
        ordering = ("-created_at",)
