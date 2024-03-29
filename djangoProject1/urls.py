"""
URL configuration for djangoProject1 project.

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
from mydj1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('New/', views.new),
    path('reverse/', views.reverse),
    path('reverse2/', views.rev),
    path('login/', views.page_auth),
    path('login/auth/', views.auth),
    path('reg/', views.page_reg),
    path('login/reg/', views.reg),
]
