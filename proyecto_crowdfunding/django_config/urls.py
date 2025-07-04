"""
URL configuration for django_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include is needed for app urls

from django.conf import settings # Para acceder a settings.DEBUG y MEDIA_URL/ROOT
from django.conf.urls.static import static # Para servir archivos media en desarrollo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/crowdfunding/', include('crowdfunding_core.urls')), # Updated app name
]

# Servir archivos media durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # It's also common to serve staticfiles this way for local dev if not using whitenoise or similar for prod-like static serving
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Optional for dev only
