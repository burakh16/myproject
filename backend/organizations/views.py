from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .serializers import SignupSerializer
from .models import Organization
from core.email import send_email


class CreateOrganizationAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        password = Organization.objects.create_organization(**validated_data)
        context = {
            "organization": validated_data["organization"],
            "name": validated_data["name"],
        }

        content = render_to_string("core/welcome.html", context)
        send_email.delay(content)
        return Response("", status=HTTP_201_CREATED)
