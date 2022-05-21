from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'ecommerce/home.html')

def catalog(request):
    return render(request, 'ecommerce/catalogs-category.html')

def cardgrading(request):
    return render(request, 'ecommerce/card-grading.html')

def marketplace(request):
    return render(request, 'ecommerce/marketplacelanding.html')

def contactus(request):
    return render(request, 'ecommerce/contact-us.html')