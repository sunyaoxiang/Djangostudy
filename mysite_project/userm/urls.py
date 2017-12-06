# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
app_name = 'userm'

urlpatterns = [
    url(r'^$', views.my_view, name='index'),
    url(r'^viewcode$', views.viewcode, name='viewcode'),
    url(r'^checkw$', views.checkwords, name='checkw'),
]