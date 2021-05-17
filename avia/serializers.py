from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)