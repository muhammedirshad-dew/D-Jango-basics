from django.shortcuts import render



def home_views(request):
    context = {'message':'Welcome to the Home page'}
    return render(request,'home.html',context)
def about_views(request):
    return render(request,'about.html')
def contact_views(request):
    return render(request,'contact.html')
def services_views(request):
    return render(request,'services.html')
