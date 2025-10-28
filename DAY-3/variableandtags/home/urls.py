from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index),
    path('about/', views.about, name='about'),
    path('hello/', views.hello, name='hello'),

]