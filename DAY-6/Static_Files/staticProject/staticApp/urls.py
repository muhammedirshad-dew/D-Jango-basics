from django.urls import path
from . import views



urlpatterns = [
    path('',views.home_views,name='home'),
    path('about/',views.about_views,name='about'),
    path('contact/',views.contact_views,name='contact'),
    path('services/',views.services_views,name='services'),
]
