from django.shortcuts import render, HttpResponse
from app.models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
   return render(request, 'about.html')
def services(request):
   return render(request, 'services.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        concern  =request.POST['concern']
        print(name,email,phone,concern)
        obj=Contact(name=name,email=email,phone=phone,concern=concern)
        obj.save()
    return render(request,'contact.html')