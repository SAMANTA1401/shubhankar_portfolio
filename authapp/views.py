from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        get_cpassword = request.POST.get('cpassword')
        if get_cpassword != get_password:
            messages.error(request, 'Password not matching')
            return redirect('/auth/signup/')
        
        print(get_email)
        print(get_password)
        print(get_cpassword)

        try:
            if User.objects.get(username=get_email):
                messages.warning(request, 'Email is taken')
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(get_email, get_email, get_password)
        myuser.save()
        messages.success(request, 'User created successfully, please Login now!')
        return redirect('/auth/login/')
    return render(request,'signup.html')

def handleLogin(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')
        myuser = authenticate(username=get_email, password=get_password)
    
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'Login Successful')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/auth/login/')

    return render(request, 'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('/')
    # return render(request, 'home.html')