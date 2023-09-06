from django.contrib import admin

from deals.models import Deals


@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display = ("customer", "item", "total", "quantity", "date")
    list_display_links = ("customer",)
    fields = (
        "customer",
        "item",
        "total",
        "quantity",
        "date",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = ["customer", "item"]
    ordering = ["-created_at"]
    list_per_page = 25