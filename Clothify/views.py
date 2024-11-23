from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to clothify!!!")


def home(request):
    return render(request, 'index.html', {})