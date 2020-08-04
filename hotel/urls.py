"""hotel URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from user.views import home, usersignup, adminsignup, booking, room, fare, userlogout, success, failure
from user.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls , name="ad"),
    
    path('',home,name="home"),
    path('booking/', booking,name="booking"),
    path('room/',room , name="room"),
    path('<int:pk>/', fare, name='fare'),
    path('success/', success, name="success"),
    path('failure/', failure, name="failure"),
    path('signup/',usersignup,name="signup"),
    path('adsignup/',adminsignup,name="adsignup"),
    path('logout/',userlogout, name='logout'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

