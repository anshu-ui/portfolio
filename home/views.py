from django.shortcuts import render
from datetime import datetime
from home.models import Connect
# Create your views here.

def index(request):
    return render(request,'index.html')


def connect(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc1 = request.POST.get("desc1")
        connect = Connect(name=name,email=email,phone=phone,desc1=desc1,date=datetime.today())
        connect.save()
    return render(request,'connect.html')