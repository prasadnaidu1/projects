"""Catering URL Configuration

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
from django.views.generic import RedirectView, TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="Welcome.html")),
    path('user/', views.userregister),
    path('userdetails/', views.userregisterdetails),
    path('userlogin/', TemplateView.as_view(template_name="UserLogin.html")),
    path('userlogindetails/', views.userlogidetails),
    path('event/',views.function),
    path('eventdetails/',views.funciondetails),

    path('itemslist/',TemplateView.as_view(template_name="FunctionType.html")),
    path('150plate/',views.plate150),
    path('200plate/',views.plate200),
    path('300plate/',views.plate300),
    path('350plate/',views.plate350),
    path('400plate/',views.plate400),

    path('adminlogin/',views.adminlogin),
    path('adminlogindetails/',views.adminlogindetails),
    path('item/',views.item),
    path('itemdetails/',views.itemdetails),

    path('plate150/',views.nonvegplate150),
    path('plate200/',views.nonvegplate200),
    path('plate300/',views.nonvegplate300),
    path('plate350/',views.nonvegplate350),
    path('plate400/',views.nonvegplate400),

    path('sweet/',views.sweetdetails),
    path('order/',views.order),
    path('orderdetails/',views.orderdetails),

    path('fb/',views.openfb),
    path('twt/',views.opentwitter),
    path('gmail/',views.opengmail),
    path('contact/',TemplateView.as_view(template_name="Contact Us.html")),




]
