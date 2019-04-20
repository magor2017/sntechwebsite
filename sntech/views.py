from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   # return HttpResponse("hello")
    return render(request,'accueil.html')
def service(request):
    return render(request,'service.html')
def realisations(request):
    return render(request,'realisations.html')
def contact(request):
    return render(request,'contact.html')
