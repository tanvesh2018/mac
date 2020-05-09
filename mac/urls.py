"""mac URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('about',views.modifiedaboutpage,name='about'),
    path('activity',views.modifiedactivitypage,name='activity'),
    path('contact',views.modifiedcontactpage,name='contact'),
    path('FAQs',views.modifiedFAQpage,name='FAQ'),
    path('gallery',views.modifiednewgallerypage,name='gallery'),
    path('team',views.modifiedteampage,name='team'),
    path('covid',views.modifiednewcovidinfo,name='covid'),
    path('donate',views.modifiednewdonatepage,name='donate'),
    path('proceed',views.proceed,name='proceed'),
    path('errorpage',views.proceed,name='errorpage'),
    path('otp',views.otp,name='otp'),
    path('errorpage2',views.otp,name='errorpage2'),
    path('sucess',views.sucess,name='sucess'),
    path('failed',views.sucess,name='failed'),


]
