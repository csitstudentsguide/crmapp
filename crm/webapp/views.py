from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, AddRecordForm, DelRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError

from . models import Record

# Create your views here.

# Home page
def home(request):
    return render(request, 'webapp/index.html')

# - Register a user
def register(request):
    
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    
    context = {'form': form}
    
    return render(request, 'webapp/register.html', context)

# - Login a user
def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context)     


# - User logout
def user_logout(request):
    
    auth.logout(request)

    return redirect('my-login')

# - User dashboard
@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'webapp/dashboard.html', context=context)

# -  Add record
@login_required(login_url='my-login')
def add_record(request):
    duplicate_email_found = False
    form = AddRecordForm()

    if request.method == 'POST':
        form = AddRecordForm(request.POST)        

        if form.is_valid():            
            email_id = form.cleaned_data['email']

            if not (Record.objects.filter(email=email_id).exists()):
                form.save()
                return redirect('dashboard')                
            else:                
                duplicate_email_found = True
                return render(request, 'webapp/add-record.html', {'form': form, 'duplicate_email_found': duplicate_email_found})
    else:                       
        return render(request, 'webapp/add-record.html', {'form': form})   












# -  Delete record
@login_required(login_url='my-login')
def del_record(request):
    form = DelRecordForm()

    if request.method == 'POST':
        form = DelRecordForm(request.POST)

        if form.is_valid():            
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            user_to_delete = Record.objects.filter(first_name=first_name, last_name=last_name, email=email)  
            user_to_delete.delete()
            return redirect('dashboard')            
    else:
        return render(request, 'webapp/del-record.html', {'form': form})

