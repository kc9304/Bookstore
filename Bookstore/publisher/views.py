from django.shortcuts import render

from .models import Personal


# Create your views here.
def vieworder(request):
    personal = Personal.objects.all()

    return render(request, 'publisher/viewdetails.html',{"personal": personal})

def home(request):
    return render(request,'publisher/home.html')


def dashboard(request):
    orders = Personal.objects.count()
    return render(request,'publisher/dashboard.html',{'orders':orders})