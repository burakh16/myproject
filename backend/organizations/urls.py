from django.urls import path

from .views import CreateOrganizationAPIView

urlpatterns = [
    path('create-organization/', CreateOrganizationAPIView.as_view(),
         name='create-organization'),
]
