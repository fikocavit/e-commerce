from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



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
            
            #user activation
            current_site=get_current_site(request)
            mail_subject='Please activate your account'
            message= render_to_string('account/account_verification_email.html', {
                'user': user,
                'domain' : current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),
            })
            to_email=email
            send_email=EmailMessage(mail_subject,message, to=[to_email])
            send_email.send()
            #user activation end
            #messages.success(request,'Registration Successful')
            return redirect('/account/login/?command=verification&email='+email)
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
    
def activate(request, uidb64, token ):
    try:
        uid= urlsafe_base64_decode(uidb64).decode()
        user= Account._defaul_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError, Account.DoesNotExist):
        user= None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        messages.success(request,'Congralations! Your account is activated')
        return redirect('login')
    else:
        messages.warning(request,'Involid Activation Link')
        return redirect('register')