"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from TheOneFitnessCenter.views import index, cadastro, login, logout, assinatura, info, info_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('assinatura', assinatura, name='assinatura'),
    path('info/<int:id>', info, name='info'),
    path('info_delete/<int:id>', info_delete, name='info_delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)