# -*- coding:utf-8 -*-
"""
__title__=''
__author__='Changer'
__created__='2018/10/11'
"""


from django.urls import path
from django.contrib import admin
from accounts import views

admin.autodiscover()

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.longin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]