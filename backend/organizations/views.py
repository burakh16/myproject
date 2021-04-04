from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OrganizationInputSerializer
from .models import Organization


class CreateOrganizationAPIView(APIView):
    def post(self, request):
        serializer = OrganizationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Organization.objects.create_organization(serializer.validated_data["name"])
        return Response("test")

