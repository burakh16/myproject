from rest_framework import serializers


class OrganizationInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)