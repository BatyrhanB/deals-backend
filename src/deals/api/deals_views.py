from rest_framework import status, response, generics, parsers

from deals.serializers.deals_serializer import FileUploadDealsSerializer, CustomerSerializer
from deals.services.deals_services import DealsService, CustomerService


class FileUploadView(generics.GenericAPIView):
    parser_classes = (parsers.MultiPartParser,)

    def post(self, request, *args, **kwargs):
        """
        Handles the file upload and processing of CSV data.

        Args:
            request: HTTP request object.
        Returns:
            Response: HTTP response indicating the success or fail error of the file upload.
        """
        file_serializer = FileUploadDealsSerializer(data=request.data)
        if file_serializer.is_valid():
            file_data = request.FILES["file"]
            success, error_message = DealsService.deals_upload_from_csv(file_data)
            if success:
                return response.Response({"status": "OK"}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopCustomersView(generics.GenericAPIView):
    """
    Returns the 5 customers who spent the highest amount during the entire period.
    Args:
        request: HTTP request object.
    Returns:
        Response: HTTP response indicating the success or fail error.
    """

    def get(self, request, *args, **kwargs) -> response.Response:
        try:
            customer_data = CustomerService.get_top_customers()
        except Exception as e:
            return response.Response({"error": str(e)}, status=500)

        serializer = CustomerSerializer(customer_data, many=True)
        return response.Response({"response": serializer.data})
