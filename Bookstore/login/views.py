from django.db.models import Q
from django.shortcuts import render
from .models import Admin, Comic, Personal


# Create your views here.
def lhome(request):
    return render(request,'login/home/home.html')
def profile(request):
    uname = request.session.get('uname')

    context = {
        'uname': uname,
    }

    return render(request, 'logout/home/profile.html',context)

def contact(request):
    return render(request,'login/home/contact.html')

def comics(request):
    return render(request,'login/home/Comics.html')
def vol1(request):
    return render(request,'login/home/vol1.html')
def vol2(request):
    return render(request,'login/home/vol2.html')
def vol3(request):
    return render(request,'login/home/vol3.html')
def vol4(request):
    return render(request,'login/home/vol4.html')
def vol5(request):
    return render(request,'login/home/vol5.html')
def hp(request):
    return render(request,'login/home/harry_potter.html')
def hvol1(request):
    return render(request,'login/home/hvol1.html')
def hvol2(request):
    return render(request,'login/home/hvol2.html')
def hvol3(request):
    return render(request,'login/home/hvol3.html')
def hvol4(request):
    return render(request,'login/home/hvol4.html')
def hvol5(request):
    return render(request,'login/home/hvol5.html')

def checkbook(request):
    name = request.GET["name"]
    flag = Comic.objects.filter(Q(name=name))
    print(flag)

    if flag:
        if name == "comic":
            return render(request, "login/home/comic.html")
        elif name == "harry potter":
            return render(request, "login/home/harry_potter.html")
        elif name == 'demon slayer vol1':
            return render(request, 'login/home/vol1.html')
        elif name == 'demon slayer vol2':
            return render(request, 'login/home/vol2.html')
        elif name == 'demon slayer vol3':
            return render(request, 'login/home/vol3.html')
        elif name == 'demon slayer vol4':
            return render(request, 'login/home/vol4.html')
        elif name == 'demon slayer vol5':
            return render(request, 'login/home/vol5.html')
        elif name == 'harry potter vol1':
            return render(request, 'login/home/hvol1.html')
        elif name == 'harry potter vol2':
            return render(request, 'login/home/hvol2.html')
        elif name == 'harry potter vol3':
            return render(request, 'login/home/hvol3.html')
        elif name == 'harry potter vol4':
            return render(request, 'login/home/hvol4.html')
        elif name == 'harry potter vol5':
            return render(request, 'login/home/hvol5.html')



  # Adjust the import based on your actual model
def form(request):
    return render(request,'login/home/form.html')

def addpersonal(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        alternate_phone = request.POST['alternate_phone']
        landmark = request.POST['landmark']
        pincode = request.POST['pincode']
        city = request.POST['city']
        town = request.POST['town']

        personal = Personal(  first_name=first_name,middle_name=middle_name,last_name=last_name, address=address,landmark=landmark,pincode=pincode,city=city,town=town, email=email,phone_number=phone, alternative_number=alternate_phone)
        personal.save()
        return render(request, "login/home/success.html")



def admin(request):
    return render(request,'login/home/admin.html')

def success(request):
    return render(request,'login/home/success.html')
def error(request):
    return render(request,'login/home/error.html')


