"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
    path('profile/',views.profile,name='profile'),
    path('login/',views.login,name='login'),
    path('index/',views.index,name='index'),
    path('soceitymembers/',views.socity_members, name='societymember'),
    path('events/',views.events, name='events'),
    path('myevent/',views.myevent, name='myevent'),
    path('visitors/',views.visitors, name='visitors'),
    path('watchman/',views.watchman, name='watchman'),
    path('notice/',views.notice, name='notice'),
    path('complaint/',views.complaint, name='complaint'),


]
