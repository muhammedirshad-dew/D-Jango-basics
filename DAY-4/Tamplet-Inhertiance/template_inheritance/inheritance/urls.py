from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_views, name='index'),
    path('base/',views.base_views, name='base'),
    path('service/',views.service_views, name='service'),
    path('blog/',views.blog_views, name='blog'),
    path('contact/',views.contact_views, name='contact'),
    path('portfolio/',views.portfolio_views, name='portfolio'),
    path('team/',views.team_views, name='team'),

]
