from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from locUnits.models import LocUnit, Event
from datetime import date, datetime
from dateutil.parser import parse

def home_view(request):
    # events = Event.objects.all()
    # for e in events:
    #     hoje = date.today()
    #     date_object = e.date.date()
    #     diferenca = hoje - date_object
    #     loc, _ = LocUnit.objects.get_or_create(name=e.locUnit)
    #     loc.days = diferenca.days
    #     loc.save()

    locUpdates = LocUnit.objects.all() 
    for e in locUpdates:
        hoje = date.today()
        date_object = e.date.date()
        diferenca = hoje - date_object
        loc, _ = LocUnit.objects.get_or_create(name=e.name)
        loc.days = diferenca.days
        loc.save()        
    
    locUnits = LocUnit.objects.all()        

    context = {
        'locUnits': locUnits
        }

    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    error_message = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')

            else:
                error_message = 'Login ou senha incorreta!'
                
    return render(request, 'login.html', {'form':form, 'error_message': error_message})
    