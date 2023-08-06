from django.shortcuts import render,HttpResponse
from atexit import register
from audioop import add
import email
from email import message
from unicodedata import name
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Register
from home.models import Feedback
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        feedback = Feedback(name=name, email=email, phone=phone, message=message, date=datetime.today())
        feedback.save()
        messages.success(request, "Your Feedback have been Recorded.")
    #return HttpResponse("this is home page")
    return render(request, 'index.html')

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone  = request.POST.get('phone')
        address = request.POST.get('address')
        qualification = request.POST.get('qualification')
        college = request.POST.get('college')
        message = request.POST.get('message')
        register = Register(name=name, email=email, phone=phone, address=address, qualification=qualification, college=college, 
                                message=message, date= datetime.today())
        register.save()
        messages.success(request, "Your Registration is successfull.")
    return render(request, 'registration.html')
