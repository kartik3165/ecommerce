from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("Welcome to clothify!!!")

def base(request):
    return render(request, 'base.html', {})


def home(request):
    return render(request, 'index.html', {})

def auth(request):
    return render(request, 'auth.html', {})

def signup(request):
    if request.method == 'POST':
        username =  request.POST['email']
        password = request.POST['password']
        full_name = request.POST['full_name']

        first_name = full_name.split(' ')[0]
        last_name = full_name.split(' ')[1]

        users = User.objects.create_user(username=username, password=password, email=username, first_name=first_name, last_name=last_name)

        print("User created Successfully !!!", users)

        return redirect('/home')

