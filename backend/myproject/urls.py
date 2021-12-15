from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include([
        path('users/', include('users.urls')),
        path('organizations/', include('organizations.urls')),
    ])),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('^.*$', TemplateView.as_view(template_name="index.html")),
]
