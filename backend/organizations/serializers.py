from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    organization = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
