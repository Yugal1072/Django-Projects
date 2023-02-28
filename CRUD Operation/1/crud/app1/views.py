from django.shortcuts import render,redirect
from app1.models import Employees


def home(request):

    emp = Employees.objects.all()

    content = {
        'emp':emp,
              }
    return render(request, 'index.html',content)

def add(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']


        emp = Employees(
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')
    return render(request,'index.html')
# Create your views here.
