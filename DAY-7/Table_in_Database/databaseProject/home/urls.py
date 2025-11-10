from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('enroll/', views.enroll_student, name='enroll_student'),
]