from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    return render(request,'pages/home.html')

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