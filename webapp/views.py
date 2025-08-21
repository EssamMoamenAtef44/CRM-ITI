from django.shortcuts import render, redirect
from django.contrib.auth import authenticate ,login , logout
from .forms import CreateUserForm, LoginForm , createRecordForm
from django.contrib.auth.decorators import login_required
from .models import Record
def index(request):
    return render(request, 'web/index.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CreateUserForm()
    return render(request, 'web/register.html', {'form': form})
#login view
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'web/login.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
   records = Record.objects.all()
   
   return render(request, 'web/dashboard.html', {'records': records})



def create_record(request):
    form = createRecordForm()
    if request.method == 'POST':
        form = createRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    else:
        form = createRecordForm()

    return render(request, 'web/create_record.html', {'form': form})

def logout(request):
        return redirect('login')