
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                    email=email, username=username, password=password )

            user.phone_number = phone_number
            print(user)
            if request.GET['candidate'] == 'designer':
                user.is_designer = True
                user.save()
                return redirect('designer-register')
            elif request.GET['candidate'] == 'recruiter':
                user.is_recruiter = True
                user.save()
                return redirect('recruiter-register')
            
            user.save() 
            print('user created')
            return redirect('accounts/login')
            context = {
                "form": form,
            }
    else:
        try:
            if request.GET['candidate'] is not None:
                form = RegisterForm()
                context = {
                    "form": form,
                }
                return render(request, 'accounts/register.html', context=context)
        except:
            return render(request, 'accounts/pre-register.html')
    
    
    return render(request, 'accounts/pre-register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        

    return render(request, 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')


