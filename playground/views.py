from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(request):
        
    return render(request, 'index.html')
def about_page(request):

    return render(request, 'about-us.html')

def contact_page(request):

    return render(request, 'contact-us.html')

def service_page(request):

    return render(request, 'our-services.html')
