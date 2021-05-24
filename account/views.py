from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            password=form.cleaned_data['password']
            username=email.split('@')[0]
            
            user=Account.objects.create_user(last_name=last_name,first_name=first_name,email=email,password=password,username=username)
            user.phone_number=phone_number
            user.save()
            messages.success(request,'Registration Successful')
            return redirect('register')
    else:
        form=RegistrationForm()
    
    return render(request, 'register.html',context={
        'form': form
    })

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        
        user=auth.authenticate(email=email,password=password)
        
        if user is not None:
            auth.login(request,user)
            #messages.success(request,'You are now logged in!')
            return redirect('store')
        else:
            messages.warning(request,'Invalid Login!')
            return redirect('login')
    return render(request, 'signin.html',context={})
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'Your are logout')
    return redirect('login')
    
    