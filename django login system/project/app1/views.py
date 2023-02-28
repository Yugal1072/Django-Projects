from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def homepage(request):
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password'] 

        if pass1 != pass2:
            return HttpResponse('Your Passwords are not matched')
        else:
            my_user = User.objects.create_user(uname,email,pass2)
            my_user.save()
            return redirect('login')
            # return redirect('login')
            

    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        all_user = authenticate(request,username= username1, password= password1)
        if all_user is not None:
            login(request,all_user)
            return redirect('homepage')
        else:
            return HttpResponse("Username or password is incorrect")
            
    return render(request,'login.html')

# Create your views here.
