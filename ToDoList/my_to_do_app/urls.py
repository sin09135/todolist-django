# my_to_do_app > urls.py
#-*- coding:UTF-8 -*- 

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index)
]