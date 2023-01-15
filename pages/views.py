from django.shortcuts import render
from . import models
from cars.models import Car

# Create your views here.
def home(request):
    team_members = models.Team.objects.all()
    cars = Car.objects.order_by('-created_date').filter(is_featured = True)
    all_cars = Car.objects.order_by('-created_date')
    context = {
        'team_members':team_members,
        'cars':cars,
        'all_cars':all_cars
    }
    return render(request,'pages/home.html',context)

def about(request):
    team_members = models.Team.objects.all()
    context = {
        'team_members':team_members
    }
    return render(request,'pages/about.html',context)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')