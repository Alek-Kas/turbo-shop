# from django.conf.urls import re_path
from django.urls import path
from . import views

app_name = 'orders'
"""
urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
]
"""
urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]
