"""
URL configuration for DR_SERVE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .import views
app_name = 'HospitalApp'  
urlpatterns = [
    path('', views.Home,name='Home'),
    path('Management/', views.Management,name='Management'),

    path('About/', views.About,name='About'),
    path('Signin/', views.Signin,name='Signin'),
    path('Make_Payment/', views.Make_Payment,name='Make_Payment'),
    path('Register/', views.Register,name='Register'),
    path('Forgot_Password/', views.Forgot_Password,name='Forgot_Password'),
    path('Whats_new/', views.Whats_new,name='Whats_new'),

    path('Contactus/', views.Contactus,name='Contactus'),









    

]
