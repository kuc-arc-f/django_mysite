#from django.conf.urls import url, include
#from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),   # 一覧
    path('book/', views.book_list, name='book_list'),
    path('book_test/', views.book_test , name='book_test' ), 
]

    