"""kk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from . import ip_operation

urlpatterns = [
    
    path('admin/', ip_operation.admin),
    path('ip_add/', ip_operation.ip_add),
    path('ip_delete/',ip_operation.ip_delete),
    path('edit_ip_gain/',ip_operation.edit_ip_gain),
    path('ip_edit/',ip_operation.ip_edit),
    path('ip_select/',ip_operation.ip_select),
]
