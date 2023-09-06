from django.urls import path

from deals.api.deals_views import FileUploadView, TopCustomersView


urlpatterns = [
    path("upload_file/", FileUploadView.as_view(), name="deals-post-file-upload"),
    path("top_customers/", TopCustomersView.as_view(), name="top-customers-list"),
]
