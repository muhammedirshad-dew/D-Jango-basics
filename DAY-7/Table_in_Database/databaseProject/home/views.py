from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student, Enrollment
from .forms import StudentForm, EnrollmentForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'home/course_list.html', {'courses': courses})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'home/student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'home/student_form.html', {'form': form})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    return render(request, 'home/course_detail.html', {'course': course, 'enrollments': enrollments})

def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = EnrollmentForm()
    return render(request, 'home/enroll_form.html', {'form': form})