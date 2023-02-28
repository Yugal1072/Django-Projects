from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def home(request):

    emp = (
        Employees.objects.all()
    )
    
    content = {
        'emp': emp
    }
    return render(request, 'index.html',content)