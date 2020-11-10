from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("todo.core.api.urls")),
    path('openapi/', get_schema_view(
        title="TODO",
        description="API for the TODO application"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
