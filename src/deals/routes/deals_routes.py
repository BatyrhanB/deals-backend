from django.urls import path

from deals.api.deals_views import FileUploadView


urlpatterns = [
    path("upload_file/", FileUploadView.as_view(), name="deals-post-file-upload"),
]
