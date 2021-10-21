from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def dorm(request):
    return render(request, 'main/dorm.html')


def education(request):
    return render(request, 'main/education.html')


def activism(request):
    return render(request, 'main/activism.html')


def wiki(request):
    return render(request, 'main/wiki.html')