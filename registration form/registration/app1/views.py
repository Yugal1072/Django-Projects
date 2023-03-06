from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homepage(request):
    return render(request,'index.html')

def signUp(request): 
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            return HttpResponse("Your Password and confirm password are not same")
        
        else:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            return redirect('login')
    else:
        print("Hello smthing is not right")

    return render(request,'register.html')


def loginPage(request):
    
    if request.method=="POST":
        
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request,username=username1, password=password1)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse('Username or Password is incorrect!')    
    
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

# Create your views here.
