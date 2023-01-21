from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method =='POST':
        car_id = request.POST['car_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            if Contact.objects.filter(user_id=user_id,car_id=car_id).exists():
                messages.error(request,"You have already made a Inquiry for this car")
                return redirect('car_details', id = car_id)

        Contact.objects.create(first_name=first_name,
        last_name=last_name,
        customer_need=customer_need,
        car_title=car_title,
        city=city,
        state=state,
        email=email,
        phone=phone,
        message=message,
        user_id=user_id,
        car_id=car_id
        ).save()

        users = User.objects.filter(is_superuser=True)
        to_email = []
        for user in users:
            to_email.append(user.email) 
        subject= "New Car Inquiry"
        message = f"You have a new car inquiry for {car_title}.For mail information kindly check from the admin panel"
        EmailMessage(subject,message,to=to_email).send()
        messages.success(request,'Youe request has been submitted and we will get back to you shortly !!')
        return redirect('car_details', id = car_id)
    else:
        return redirect('car_details', id = car_id)