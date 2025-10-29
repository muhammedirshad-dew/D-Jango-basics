from django.shortcuts import render

# Create your views here.
def base_views(request):
    return render(request, 'base.html')

def service_views(request):
    return render(request, 'service.html')

def blog_views(request):
    return render(request, 'blog.html')

def contact_views(request):
    return render(request, 'contact_us.html')

def index_views(request):
    return render(request, 'index.html')

def portfolio_views(request):
    return render(request, 'portfolio.html')

def team_views(request):
    return render(request, 'team.html')

