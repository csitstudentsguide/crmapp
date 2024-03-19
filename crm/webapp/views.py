from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
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
            #return redirect()
    
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
                #return redirect()
    
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context)

        
