from django.shortcuts import render
from .models import *

# Create your views here.
def register_details(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    s1=Register(id,name)
    s1.save()
    return render(request,"index.html")


def register_d(request):
    res=Register.objects.last.values("id")
    print(res)
    id=0
    if res==[]:
        id=101
    else:
        for x in res:
            print(x)
            id=x
    id=int(id)+1
    return render(request,"index.html",{"id":id})