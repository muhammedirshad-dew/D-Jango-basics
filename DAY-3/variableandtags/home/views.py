from django.shortcuts import render

# Create your views here.

def index(request):
    person ={
    'name': 'john',
    'age': 30,
    'city': 'calicut'
    }
 
    return render(request, 'index.html', person)

def about(request):
    number = {
    'num1': 0,
    'num2': 20
    }
    return render(request, 'about.html', number)


def hello(request):
    number = {
        'num1': [1,2,3,4,5,6,7,8,9,10],
        'fruit': ['apple', 'banana', 'mango', 'grape']
    }
    return render(request, 'hello.html', number)
