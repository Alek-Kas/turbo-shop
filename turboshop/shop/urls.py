# from django.conf.urls import url
# from django.template.defaulttags import url
from django.urls import path, re_path
from . import views

# app_name = 'shop'
"""
urlpatterns = [
    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
"""

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'),
]
