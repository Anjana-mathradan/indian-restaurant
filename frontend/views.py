from django.shortcuts import render,redirect
from backend.models import categorydb,productdb,frontregisterdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def fnindex(request):
    data=categorydb.objects.all()
    return render(request,"fnindex.html", {'data':data})

def fncontact(request):
    data = categorydb.objects.all()
    return render(request,"fncontact.html", {'data':data})
def fnabout(request):
    data = categorydb.objects.all()
    return render(request,"fnabout.html", {'data':data})

def displaycategorypage(request,itemcategory):
    data=categorydb.objects.all()
    products=productdb.objects.filter(PCategory=itemcategory)

    context={

        'data':data,
        'products':products
    }
    return render(request,"categorydisplay.html",context)




def singleproduct(request,dataid):
    data=productdb.objects.get(id=dataid)
    da=categorydb.objects.all()
    return render(request,"product.html" ,{'dat':data,'da':da})


def frontreg(request):
    return render(request,"frontreg.html")
def registersave(request):
    if request.method == "POST":
        usrname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password==cpassword:
            obj=frontregisterdb(Username=usrname,Email=email,Password=password,Cpassword=cpassword)
            obj.save()
            return redirect(frontlogin)
        else:
            return render(request,"fontreg.html",{'msg':"Password Does Not Match. Please Sign In Again!"})

def frontlogin(request):
    return  render(request,"frontlogin.html")

def frontloginsave(request):
    if request.method=="POST":
        username_a=request.POST.get('username')
        password_a=request.POST.get('password')
        if frontregisterdb.objects.filter(Username=username_a,Password=password_a).exists():
               request.session['username']=username_a
               request.session['password']=password_a
               return redirect(fnindex)
        else:
               return redirect(frontlogin)
    else:
        return redirect (fnindex)
def frontlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logged Out Successfully !!!")
    return redirect(fnindex)
