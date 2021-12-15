from django.urls import path

from .views import CreateOrganizationAPIView

urlpatterns = [
    path('create/', CreateOrganizationAPIView.as_view(),
         name='create'),
]
