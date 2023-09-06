from rest_framework import serializers


class FileUploadDealsSerializer(serializers.Serializer):
    file = serializers.FileField()