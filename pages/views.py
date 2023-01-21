from django.shortcuts import render
from . import models
from cars.models import Car
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    team_members = models.Team.objects.all()
    cars = Car.objects.order_by('-created_date').filter(is_featured = True)
    all_cars = Car.objects.order_by('-created_date')
    year_values = Car.objects.values_list('year',flat=True).distinct()
    model_values = Car.objects.values_list('car_title',flat=True).distinct()
    state_values = Car.objects.values_list('state',flat=True).distinct()
    type_values = Car.objects.values_list('body_style',flat=True).distinct()
    context = {
        'team_members':team_members,
        'cars':cars,
        'all_cars':all_cars,
        'year_values':year_values,
        'model_values':model_values,
        'state_values':state_values,
        'type_values':type_values
        
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        users = User.objects.filter(is_superuser=True)
        admin_message = f"Hi Admin , recieved message from {name} .Kindly check on it his phone number is :{phone} and email: {email} His message {message}"
        to_email = []
        for user in users:
            to_email.append(user.email)
        EmailMessage(subject,admin_message,to=to_email).send()
        user_subject = "From Car Zone"
        user_message = f"Hi {name},Thanks for contacting us we will check and get back to you"
        user_to_email = []
        user_to_email.append(email)
        EmailMessage(user_subject,user_message,to=user_to_email).send()
        messages.success(request,"Successfuly send")

        return render(request,'pages/contact.html')
    else:
        return render(request,'pages/contact.html')