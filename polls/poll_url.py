#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pycharm.
# User: y1wanghui@163.com
# Date  : 2018/6/29
# Desc  :

from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('liuyintao/',views.do_app),
    path('wang/',views.do_wang),
    path('',views.do_home),
    path('count/',views.do_count),
    path('double/',views.do_double),

]
