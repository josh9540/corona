"""corona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from . import views
from .views import pathtracing
from rest_framework import routers
urlpatterns = [
    path('test/',views.test, name = "test"),
    path('table/',views.table, name= "table"),
    path('inputLocation',views.inputLocation, name= "inputLocation"),
    path('register/',views.register, name= "register"),
    path('updateUserDetail/',views.updateUserDetail,name="updateUserDetail"),
    path('admin_add_user_detail/',views.admin_add_user_detail, name= "admin_add_user_detail"),
    path('pathtracing/<int:user_id>/',pathtracing,name = "pathTracing"),
    path('search_user/',views.search_user, name = "search_user"),
]
