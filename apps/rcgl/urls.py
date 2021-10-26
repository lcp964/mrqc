from django.urls import path
from . import  views

urlpatterns = [
    path('',views.login.as_view()),
    path('index/', views.index.as_view(),name='index'),
    path('index/add/', views.OrderRgister.as_view(), name='order'),
]