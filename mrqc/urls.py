"""mrqc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from apps import rcgl

admin.AdminSite.site_header = 'bp神经网络汽车美容管理系统'
admin.AdminSite.site_title ='bp神经网络汽车美容管理系统'
urlpatterns = [
    path('', admin.site.urls),
    path('',include('apps.rcgl.urls'))
]

