from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from app.models import addstate


def Adminlogin(request):
    a_user=request.POST.get("u1")
    a_pass=request.POST.get("u2")
    if a_user=="prasad" and a_pass=="prasad":
        return render(request,"Admin-Home.html")
    else:
        return render(request,"Admin-Login.html")
class viewstate(CreateView):
    model = addstate
    template_name = "Admin-State.html"
    fields = ['id','name']
    def form_valid(self, form):
        form.save()
        return HttpResponse("Registred Successfully")
    def form_invalid(self, form):
        return HttpResponse("Not Saved")
class viewstatedetails(ListView):
    model=addstate
    template_name = "Admin-State.html"


