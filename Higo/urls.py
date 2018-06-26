"""Higo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from hgo import views
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.hgo_list),
    path('insert/', views.hgo_insert, name="hgo_insert"),
    path('del/', views.delById, name="hgo_del"),
    path('query/', views.queryById, name="hgo_query"),
    path('add/', views.upById, name="hgo_add"),
]
