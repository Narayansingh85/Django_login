from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    if request.method =='POST':
        if 'register-form-button' in request.POST:
            # Registering data
            first_name= request.POST['first_name']
            last_name= request.POST['last_name']
            username= request.POST['username']
            password= request.POST['password']
            password2= request.POST['password2']
            email= request.POST['email']

            # Check if password match
            if password == password2:
                # Check username
                if User.objects.filter(username=username).exists():
                    return render(request,'front/index.html')
                else:
                    if User.objects.filter(email=email).exists():
                        return render(request,'front/index.html')
                    else:
                        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                        user.save()
                        print('save nahi  hua')
                        return render(request,'front/index.html')
            else:
                print('password does not match')
                return redirect('index.html')

        elif 'login-form-button' in request.POST:
            if request.method=='POST':
                username=request.POST['username']
                password=request.POST['password']

                user=auth.authenticate(username=username,password=password)

                if user is not None:
                    auth.login(request,user)
                    return redirect('loggedin')
                elif user is None:
                    redirect('index')
                else:
                    redirect('index')
                return render(request,'front/index.html')
    else:
        return render(request,'front/index.html')

def login(request):
    return render(request,'final/loggedin.html')