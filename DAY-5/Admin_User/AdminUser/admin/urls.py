from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_viewa, name='home'),
    path('services/',views.services_view, name='services'),
    path('portfolio/',views.portfolio_view, name='portfolio'),
    path('team/',views.team_view, name='team'),
    path('blog/',views.blog_view, name='blog'),
    path('contact/',views.contact_view, name='contact'),
]