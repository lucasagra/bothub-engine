from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from bothub.api.routers import router as bothub_api_routers

urlpatterns = [
    path('api/', include(bothub_api_routers.urls)),
    path('docs/', include_docs_urls(title='API Documentation')),
    path('admin/', admin.site.urls),
]