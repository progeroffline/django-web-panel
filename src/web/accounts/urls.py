# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
     path('sign_up/', views.sign_up_view, name='sign_up'),
     path('login/', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout'),

]
