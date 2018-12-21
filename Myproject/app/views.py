from django.shortcuts import render

from app.models import adddoctor


def adminlogindetails(request):
    username=request.POST.get("u1")
    password=request.POST.get("u2")
    if username=="admin" and password=="admin":
        return render(request,"AdminHome.html")
    else:
        return render(request,"AdminLogin.html")


def adminlogout(request):
    return render(request,"Index.html")


def doctorregister(request):
    return render(request,"AddDoctor.html")


def doctor_details(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    email=request.POST.get("t3")
    password=request.POST.get("t4")
    exp=request.POST.get("t5" )
    dept=request.POST.get("t6")
    s1=adddoctor(name,cno,email,password,exp,dept)
    s1.save()
    return render(request,"AddDoctor.html")