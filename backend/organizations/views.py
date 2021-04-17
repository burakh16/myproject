from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .serializers import OrganizationInputSerializer
from .models import Organization
from core.email import send


class CreateOrganizationAPIView(APIView):
    def post(self, request):
        #serializer = OrganizationInputSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #Organization.objects.create_organization(
        #    serializer.validated_data["name"])
        send.delay()
        return Response("", status=HTTP_201_CREATED)
