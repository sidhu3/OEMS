"""
URL configuration for office_emp project.

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
# from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all_emp',views.all_emp,name='all_emp'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('remove_emp',views.remove_emp,name='remove_emp'),
    path('remove_emp/<int:pk>',views.remove_emp,name='remove_emp'),
    path('filter_emp',views.filter_emp,name='filter_emp'),
    path('accounts/logout/',views.logout_view),
    path('signup/',views.signup_view),
    path('accounts/',include('django.contrib.auth.urls')),

    path('update/<int:pk>',views.UpdateEmployee_view.as_view()),
    path('delete/<int:pk>/', views.DeleteEmployee.as_view()),
    path('list/', views.Employee_list_view.as_view(),name='list'),

]

