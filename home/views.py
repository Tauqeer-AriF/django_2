from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render( request, 'index.html')

def about(request):
    return render( request, 'about.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(fname=fname, lname=lname, email=email, phone=phone, message=message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Sent!')
    return render( request, 'contact.html')
