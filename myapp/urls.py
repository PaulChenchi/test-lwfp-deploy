"""
URL configuration for LWF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from myapp import views
from django.conf import settings
from django.urls import re_path as url
import django.contrib.auth.views as auth_view
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings

urlpatterns = [
    path('', views.ex_index, name = 'ex_index'), #首頁
    # url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    # path('base/', views.base, name = 'base'), #模板
    path("register/", views.register, name="register"), #註冊
    path("register/add/", views.regadd, name="regadd"), #註冊成功
    path("login/", views.login, name="login"), #登入
    path("logout/", views.logout, name="logout"), #登出
    path('ex_fashion_3C/', views.ex_fashion_3C, name="ex_fashion_3C"),
    path('ex_fashion_colthing/', views.ex_fashion_colthing, name="ex_fashion_colthing"),
    path('ex_fashion_pet/', views.ex_fashion_pet, name="ex_fashion_pet"),
    path('ex_fashion_Srationery/', views.ex_fashion_Srationery, name="ex_fashion_Srationery"),
    path('ex_fashion_daily/', views.ex_fashion_daily, name="ex_fashion_daily"),
    path('search/', views.search, name="search"), #搜尋
    # path('index/', views.index, name="index"), 
    

]
# urlpatterns += staticfiles_urlpatterns()