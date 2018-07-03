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
    path('home/',views.do_home),
    #计算字数url
    path('home/count/',views.do_count),
    #返回主页 url
    path('home/double/',views.do_double),
    # ex: /polls/
    path('',views.index,name='index'),
    #ex: /pools/5/
    path('<int:question_id>/',views.detail,name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results',views.result,name='result'),
    #ex:ex: /polls/5/vote/
    path('<int:question_id>/vote/',views.vote,name='vote'),

]
