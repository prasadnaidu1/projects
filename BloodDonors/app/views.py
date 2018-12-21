from django.shortcuts import render
from app.models import *
def adminlogindetails(request):
    a_name=request.POST.get("u1")
    a_pass=request.POST.get("u2")
    if a_name=="prasad" and a_pass=="prasad":
        return render(request,"AdminHomePae.html")
    else:
        return render(request,"AdminLogin.html")

def addcities(request):
    res1 = addcity.objects.all()
    print(res1)
    return render(request,"Addcity.html",{"res1":res1})


def citydetails(request):
    id=request.POST.get("c1")
    state=request.POST.get("c2")
    city=request.POST.get("c3")
    s1=addcity(id,state,city)
    s1.save()
    res1 = addcity.objects.all()
    return render(request,"AddCity.html")

def addstates(request):
    res = addstate.objects.all()
    print(res)
    return render(request,"AddState.html",{"res":res})


def statedetails(request):
    id = request.POST.get("c1")
    state = request.POST.get("c2")
    s2=addstate(id,state)
    s2.save()
    res=addstate.objects.all()
    return render(request,"AddState.html",{"res":res})
def add_donors(request):
    res3 = Adddonor.objects.all()
    print(res3)
    return render(request, "AddDonor.html", {"res3": res3})

def donordetails(request):
    name=request.POST.get("d1")
    cno=request.POST.get("d2")
    email=request.POST.get("d3")
    password=request.POST.get("d4")
    s3=Adddonor(name,cno,email,password)
    s3.save()
    res3 = Adddonor.objects.all()
    return render(request,"AddDonor.html", {"res3": res3})

def donor_delete_details(request):
    id=request.POST.get("delete_id")
    Adddonor.objects.filter(cno=id).delete()
    return add_donors(request)

def donor_update_details(request):
    email=request.GET.get("update_id")

    Adddonor.objects.filter(email=email).update()
    return render(request,"AddDonor.html",{"email":email})


def add_org(request):
    res4 = Addorg.objects.all()
    print(res4)
    return render(request, "AddOrganisation.html", {"res4": res4})

def orgdetails(request):
    name = request.POST.get("d1")
    cno = request.POST.get("d2")
    email = request.POST.get("d3")
    password = request.POST.get("d4")
    s3 = Addorg(name, cno, email, password)
    s3.save()
    res4 = Adddonor.objects.all()
    return render(request, "AddOrganisation.html")
def org_delete(request):
    id=request.POST.get("delete_id")
    Addorg.objects.filter(email=id).delete()
    return add_org(request)


def org_update(request):
    email=request.GET.get("update_id")
    Addorg.objects.filter(email=email).update()
    return  render(request,"AddOrganisation.html",{"mail":email})


def sugdetails(request):
    sug=request.POST.get("r1")
    choice=request.POST.get("r2")
    s4=suggetions(sug=sug,choice=choice)
    s4.save()
    return render(request,"Suggetions.html")






