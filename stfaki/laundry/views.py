from django.shortcuts import render, redirect
from .models import signups
from .forms import signupsForm

# Create your views here.
def index(request):
    signup = signups.objects.order_by('datetime')
    return render(request, 'laundry/laundry_home.html', {'signup' : signup})

def check(request):
    error = ''
    if request.method == "POST":
        form = signupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laundry_home')
        else:
            error = "Введены некорректные данные"

    form = signupsForm()
    data = {
        'form' : form,
        'error': error,
    }

    return render(request, 'laundry/check.html', data)
