from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Admin, Book
from django.contrib.auth.models import User


# Create your views here.
def base(request):
    return render(request,'logout/home/home.html')

def checklogin(request):
    uname = request.POST["uname"]
    password = request.POST["pwd"]
    flag = Admin.objects.filter(Q(username=uname) & Q(password=password))
    request.session['uname'] = uname
    print(flag)
    if flag and uname == "Krishna":
        return redirect('phome')
    if flag:
        return redirect('lhome')
    else:
        return redirect('error')

def profile(request):
    uname = request.session.get('uname')

    context = {
        'uname': uname,
    }

    return render(request, 'login/home/profile.html',context)

def addregister(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pwd']
        password2=request.POST['pwd2']

        email=request.POST['email']
        new_id = Admin(username=uname,password=password,email=email)
        request.session['uname'] = uname
        new_id.save()
        return redirect('home')




class RegistrationForm(forms.Form):
    uname = forms.CharField(max_length=50, required=True, label="Username")
    pwd = forms.CharField(widget=forms.PasswordInput, label="Password")
    pwd2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    email = forms.EmailField(label="Email")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('pwd')
        password2 = cleaned_data.get('pwd2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")




def addregister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['uname']
            password = form.cleaned_data['pwd']
            email = form.cleaned_data['email']

            # Check if the user already exists
            if Admin.objects.filter(username=uname).exists():
                return render(request, 'registration_error.html', {'message': 'User already exists.'})

            new_id = Admin(username=uname, password=password, email=email)
            new_id.save()
            request.session['uname'] = uname
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def cart(request):

    return render(request,'logout/home/cart.html')


