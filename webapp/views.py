from django.shortcuts import render, redirect ,get_object_or_404
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



@login_required(login_url='login')
def create_record(request):
    if request.method == 'POST':
        form = createRecordForm(request.POST)
        if form.is_valid():
            try:
                record = form.save(commit=False)
                if request.user.is_authenticated:
                    record.save()
                    return redirect('dashboard')
            except Exception as e:
                print(f"Error saving record: {e}")
        else:
            print("Form errors:", form.errors)
    else:
        form = createRecordForm()

    return render(request, 'web/create_record.html', {'form': form})
@login_required(login_url='login')
def view_record(request, record_id):
    all_records = get_object_or_404(Record, id=record_id)
    return render(request, 'web/view_record.html', {'record': all_records} )

def logout(request):
        return redirect('login')