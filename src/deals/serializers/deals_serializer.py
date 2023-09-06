from rest_framework import serializers


class FileUploadDealsSerializer(serializers.Serializer):
    file = serializers.FileField()


class CustomerSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    spent_money = serializers.IntegerField(read_only=True)
    gems = serializers.ListField(child=serializers.CharField())
