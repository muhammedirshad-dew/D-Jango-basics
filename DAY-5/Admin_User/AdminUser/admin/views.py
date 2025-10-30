from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home_viewa(request):
    return render(request, 'home.html')
def services_view(request):
    return render(request, 'services.html')
def portfolio_view(request):
    return render(request, 'portfolio.html')
def team_view(request): 
    return render(request, 'team.html')
def blog_view(request):
    return render(request, 'blog.html')
def contact_view(request):
    return render(request, 'contact.html')
