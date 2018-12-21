"""BloodDonors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="Showindex.html")),
    path('adminlogin/', TemplateView.as_view(template_name="AdminLogin.html")),
    path('adminlogindetails/',views.adminlogindetails),

    path('citydetails/',views.citydetails),
    path('addcity/', views.addcities),

    path('addstate/', views.addstates),
    path('statedetails/', views.statedetails),

    path('adddonor/', views.add_donors),
    path('donordetails/', views.donordetails),
    path('donordelete/', views.donor_delete_details),
    path('donorupdate/', views.donor_update_details),


    path('addorg/', views.add_org),
    path('orgdetails/', views.orgdetails),
    path('orgdelete/', views.org_delete),
    path('orgupdate/', views.org_update),

    path('addsug/', TemplateView.as_view(template_name="Suggetions.html")),
    path('sugdetails/', views.sugdetails)


]
