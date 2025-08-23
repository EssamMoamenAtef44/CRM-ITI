from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import CreateUserForm, LoginForm, createRecordForm, updateRecordForm
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
import logging
from django.contrib import messages

def index(request):
    return render(request, 'web/index.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')  
    else:
        form = CreateUserForm()
    return render(request, 'web/register.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
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
                # Print form data for debugging
                print("Form data:", request.POST)
                record.save()
                messages.success(request, 'Record created successfully!')
                return redirect('dashboard')
            except Exception as e:
                print("Error saving record:", str(e))  # Debug print
                messages.error(request, f'Error creating record: {str(e)}')
        else:
            print("Form errors:", form.errors)  # Debug print
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = createRecordForm()
    
    return render(request, 'web/create_record.html', {'form': form})



@login_required(login_url='login')
def view_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    return render(request, 'web/view_record.html', {'record': record})



@login_required(login_url='login')
def update_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = updateRecordForm(instance=record)
    if request.method == 'POST':
        form = updateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully.')
            return redirect('dashboard')
    return render(request, 'web/update_record.html', {'form': form, 'record': record})



@login_required(login_url='login')
def delete_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('dashboard')
    return render(request, 'web/delete_record.html', {'record': record})



def search_records(request):
    search_query = request.POST.get('searched', '') if request.method == 'POST' else request.GET.get('query', '')
    records = []
    
    if search_query:
        try:
            records = Record.objects.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(address__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(category__name__icontains=search_query)
            )
        except Exception as e:
            logging.error(f"Error during search: {e}")
    
    context = {
        'searched': search_query,
        'records': records,
        'query': search_query
    }
    return render(request, 'web/search.html', context)



def logout(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


def custom_404_view(request, exception):
    return render(request, 'web/404.html', status=404)