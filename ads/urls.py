#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'ads'

urlpatterns = [
    # Create a ad
    path('create/', views.AdCreateView.as_view(), name='ad_create'),
    # Retrieve ad list
    path('', views.AdListView.as_view(), name='ad_list'),
    # Retrieve single ad object
    re_path(r'^(?P<pk>\d+)/$', views.AdDetailView.as_view(), name='ad_detail'),
    # Update a ad
    re_path(r'^(?P<pk>\d+)/update/$', views.AdUpdateView.as_view(), name='ad_update'),
    # Delete a ad
    re_path(r'^(?P<pk>\d+)/delete/$', views.AdDeleteView.as_view(), name='ad_delete')
]