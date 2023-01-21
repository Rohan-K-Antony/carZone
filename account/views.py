from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                print(user.username)
                return redirect('dashboard')
            else:
                print('Error message')
                messages.error(request,'Invalid Credential')
                return redirect('login')
        else:
            return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

    

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['confirm_password']
        
        if password != c_password:
            print(f'{password} -> {c_password}')
            messages.error(request,"PASSWORD DOES NOT MATCH !!")
            return redirect('register')
        else:
            if User.objects.filter(username = user_name).exists():
                messages.error(request,"UserName Already Exists")
                return redirect('register')
            else:
                if User.objects.filter(email__iexact = email).exists():
                    messages.error(request,"Email Already Exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=user_name,email=email,first_name=first_name,last_name=last_name)
                    user.set_password(password)
                    user.save()
                    messages.success(request,'Registration is successfuly !!!')
                    return redirect('login')
    else:
        return render(request,'accounts/register.html')

@login_required(login_url = 'login' )
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-created_date').filter(user_id =request.user.id )
    context ={
        'user_inquiry':user_inquiry
    }
    return render(request,'accounts/dashboard.html',context)