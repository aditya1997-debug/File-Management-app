"""
URL configuration for file_manager_project project.

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
from django.urls import path
from file_manager import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('users/', views.custom_user_list, name='custom_user_list'),
    path('users/<int:pk>/', views.custom_user_detail, name='custom_user_detail'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('files/', views.file_list, name='file_list'),
    path('files/<int:pk>/', views.file_detail, name='file_detail'),
    path('folders/', views.folder_list, name='folder_list'),
    path('folders/<int:pk>/', views.folder_detail, name='folder_detail'),
    path('files/<int:file_id>/share/<int:user_id>/', views.share_file, name='share_file'),
    path('files/download/<str:file_name>/', views.file_by_name, name='file_by_name'),

]
