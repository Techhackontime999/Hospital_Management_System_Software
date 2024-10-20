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
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name='Home'),
    path('About/', views.About,name='About'),
    path('Pricing/', views.Pricing,name='Pricing'),
    path('Contactus/', views.Contactus,name='Contactus'),
    path('Whats_new/', views.Whats_new,name='Whats_new'),
    path('Learn_more/', views.Learn_more,name='Learn_more'),




  



    


    # include app here
     path("HospitalApp/",  include(('HospitalApp.urls', 'HospitalApp'), namespace='HospitalApp')),
     path("MediJeevan/", include("MediJeevan.urls",namespace="Medijeevan")),
     path("DR_BLOG/", include("DR_BLOG.urls",namespace="DR_BLOG")),
     path("DR_Feature/", include("DR_Feature.urls",namespace="DR_Feature")),
     path("DRAppoint/", include("DRAppoint.urls",namespace="DRAppoint")),


# urlpatterns = [
#     path('HospitalApp/', include(('HospitalApp.urls', 'HospitalApp'), namespace='HospitalApp')),
# ]



    #  always put below in last
     path("__reload__/", include("django_browser_reload.urls")),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
