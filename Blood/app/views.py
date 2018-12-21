from django.shortcuts import render
from .models import addstate
from .models import addscity


def openDonorlogin(request):
    type=request.GET.get("type")

    return render(request,"Index.html",{"type":type})


def openHome(request):
    return render(request,"Index.html")


def openOrganisationlogin(request):
    type=request.GET.get("type")
    return render(request,"Index.html",{"type":type})


def Home(request):
    type="home"
    return render(request,"Index.html",{"type":type})


def newdonor(request):
    type=request.GET.get("type")
    states=[]
    res = addstate.objects.values('state')
    for x in res:

        states.append(x['state'])
    #cities=[]
    #res1=addscity.objects.values("city")
    #for y in res1:
        #cities.append(y["city"])

    return render(request,"Index.html",{"type":type,"state":states,})


def getCityFromState(request):
    d_state=request.GET.get("state")
    print(d_state)
    res=addstate.objects.values('id').filter(state=d_state)

    print(res)
    return None