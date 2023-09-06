from django.urls import path, include

urlpatterns = [
    path("deals/", include("deals.routes.deals_routes"), name="main-deals"),
]
