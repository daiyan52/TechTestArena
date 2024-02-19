from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import *  
from django.http import HttpResponseRedirect
# Create your views here.
def homeView(request):
    return render(request, 'pages/home.html')

@login_required
def javaView(request):
    return render(request, 'pages/java.html')

@login_required
def pythonView(request):
    return render(request, 'pages/python.html')

@login_required
def aptitudeView(request):
    return render(request, 'pages/Aptitude.html')

def logoutView(request):
    return render(request, 'pages/logout.html')

def signupView(request):
    form = sighUpForm()
    if request.method == 'POST':
        form = sighUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'pages/signup.html', {'form': form})
