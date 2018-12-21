from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def userregister(request):
    return render(request,"UserRegistration.html")


def userregisterdetails(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    email=request.POST.get("t3")
    add=request.POST.get("t4")
    username=request.POST.get("t5")
    password=request.POST.get("t6")
    u1=userregisteration(name=name,cno=cno,email=email,add=add,username=username,password=password)
    u1.save()
    return render(request,"UserRegistration.html")


def userlogidetails(request):
    username=request.POST.get("e1")
    password=request.POST.get("e2")
    res=userregisteration.objects.filter(username=username,password=password)
    if res:
        return render(request,"Different_Catarings.html")
    else:
        return render(request,"UserLogin.html")


def funciondetails(request):

    food_type=request.POST.get("food")
    s2=Functiondetails(fun=food_type)
    s2.save()
    if food_type=="Veg":
        return render(request,"Veg.html")
    elif food_type=="Non-Veg":
        return render(request,"Non-Veg.html")
    else:
        return render(request,"Both.html")
def function(request):
    return render(request,"FunctionType.html")
def plate150(request):
    res=veg150.objects.all()
    return render(request,"veg/150 Plate.html",{"res":res})

def plate200(request):
    res1=veg200.objects.all()
    return render(request,"veg/200 Plate.html",{"res1":res1})

def plate300(request):
    res3=veg300.objects.all()
    return render(request,"veg/300 Plate.html",{"res3":res3})

def plate350(request):
    res4=veg350.objects.all()
    return render(request,"veg/350 Plate.html",{"res4":res4})
def plate400(request):
    res5=veg400.objects.all()
    return render(request,"veg/400 Plate.html",{"res5":res5})


def adminlogin(request):
    return render(request,"Admin/AdminLogin.html")


def adminlogindetails(request):
    admin_username=request.POST.get("u1")
    admin_password=request.POST.get("u2")
    if admin_username=="admin" and admin_password=="admin":
        return render(request,"Admin/Admin_itemAdd.html")
    else:
        return render(request,"Admin/AdminLogin.html")


def item(request):
    return render(request,"Admin/Admin_itemAdd.html")


def itemdetails(request):
    item_id=request.POST.get("i1")
    item_name=request.POST.get("i2")
    item_type=request.POST.get("i3")
    item_cost=request.POST.get("i4")
    if item_type=="Veg" and item_cost=="150Plate":
        i1=veg150(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    elif item_type=="Veg" and item_cost=="200Plate":
        i1=veg200(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    elif item_type=="Veg" and item_cost=="300Plate":
        i1=veg300(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    elif item_type=="Veg" and item_cost=="350Plate":
        i1=veg350(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    elif item_type=="Veg" and item_cost=="400Plate":
        i1=veg400(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    elif item_type=="Non-Veg" and item_cost=="150Plate":
        i1=NOnveg150(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    elif item_type=="Non-Veg" and item_cost=="200Plate":
        i1=Nonveg200(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    elif item_type=="Non-Veg" and item_cost=="300Plate":
        i1=Nonveg300(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    elif item_type=="Non-Veg" and item_cost=="350Plate":
        i1=Nonveg350(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")
    else:
        i1=Nonveg400(item_id,item_name,item_type,item_cost)
        i1.save()
        return render(request,"Admin/Admin_itemAdd.html")


def nonvegplate150(request):
    ans = NOnveg150.objects.all()
    return render(request,"Nonveg/150 Plate.html",{"ans":ans})


def nonvegplate200(request):
    ans1 = Nonveg200.objects.all()
    return render(request,"Nonveg/200 Plate.html",{"ans1":ans1})


def nonvegplate300(request):
    ans2=Nonveg300.objects.all()
    return render(request,"Nonveg/300 Plate.html",{"ans2":ans2})


def nonvegplate350(request):
    ans3 = Nonveg350.objects.all()
    return render(request,"Nonveg/350 Plate.html",{"ans3":ans3})


def nonvegplate400(request):
    ans4 = Nonveg400.objects.all()
    return render(request,"Nonveg/400 Plate.html",{"ans4":ans4})


def sweetdetails(request):
    sweet=request.POST.get("t1")
    d1=swetdetails(sweet=sweet)
    d1.save()
    return render(request,"veg/150 Plate.html")


def orderdetails(request):
    name=request.POST.get("n1")
    cno=request.POST.get("n2")
    add=request.POST.get("n3")
    food_type=request.POST.get("n4")
    delivery_date=request.POST.get("n5")
    no_of_plates=request.POST.get("n6")
    o1=orderdetail(name=name,cno=cno,d_add=add,
                   food_type=food_type,d_date=delivery_date,
                   no_plates=no_of_plates)
    o1.save()
    return render(request,"PlaceOrder.html")

def order(request):
    return render(request,"PlaceOrder.html")

def openfb(request):
    return redirect("http://www.facebook.com")

def opentwitter(request):
    return redirect("http://www.twitter.com")

def opengmail(request):
    return redirect("http://mail.google.com")