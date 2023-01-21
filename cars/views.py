from django.shortcuts import render
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = 'login' )
def cars(request):
    year_values = Car.objects.values_list('year',flat=True).distinct()
    model_values = Car.objects.values_list('car_title',flat=True).distinct()
    state_values = Car.objects.values_list('state',flat=True).distinct()
    type_values = Car.objects.values_list('body_style',flat=True).distinct()
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars,2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    context = {
        'all_cars':paged_cars,
        'year_values':year_values,
        'model_values':model_values,
        'state_values':state_values,
        'type_values':type_values
    }
    return render(request,'cars/cars.html',context)

@login_required(login_url = 'login' )
def car_details(request,id):
    car_detail = Car.objects.get(pk=id)
    context = {
        "car_detail" : car_detail
    }
    return render(request,'cars/car_details.html',context)

@login_required(login_url = 'login' )
def search(request):
    year_values = Car.objects.values_list('year',flat=True).distinct()
    model_values = Car.objects.values_list('car_title',flat=True).distinct()
    state_values = Car.objects.values_list('state',flat=True).distinct()
    type_values = Car.objects.values_list('body_style',flat=True).distinct()
    cars = Car.objects.order_by('-created_date')
    context = {
        'cars':cars,
        'year_values':year_values,
        'model_values':model_values,
        'state_values':state_values,
        'type_values':type_values
    }
    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            filter_models = Car.objects.filter(price__gte = min_price,price__lte = max_price)
            
            context ={
                'cars':filter_models,
                'year_values':year_values,
                'model_values':model_values,
                'state_values':state_values,
                'type_values':type_values
            }
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            print(keyword)
            filter_cars = Car.objects.filter(description__icontains = keyword)
            for i in filter_cars:
                print(i.car_title)
            context = {
                'cars':filter_cars,
                'year_values':year_values,
                'model_values':model_values,
                'state_values':state_values,
                'type_values':type_values
            }
            

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            filter_models = Car.objects.filter(car_title__iexact = model)
            context ={
                'cars':filter_models,
                'year_values':year_values,
                'model_values':model_values,
                'state_values':state_values,
                'type_values':type_values
            }
        
    if 'state' in request.GET:
        model = request.GET['state']
        
        if model:
            filter_models = Car.objects.filter(state__iexact = model)
            for i in filter_models:
                print(i.car_title)
            context ={
                'cars':filter_models,
                'year_values':year_values,
                'model_values':model_values,
                'state_values':state_values,
                'type_values':type_values
            }
    if 'body_type' in request.GET:
        model = request.GET['body_type']
        if model:
            filter_models = Car.objects.filter(body_style__iexact = model)
            context ={
                'cars':filter_models,
                'year_values':year_values,
                'model_values':model_values,
                'state_values':state_values,
                'type_values':type_values
            }
    if 'year' in request.GET:
        model = request.GET['year']
        print(type(model))
        if model:
            filter_models = Car.objects.filter(year__iexact = model)
            context ={
                'cars':filter_models,
                'year_values':year_values,
                'model_values':model_values,
                'state_values':state_values,
                'type_values':type_values
            }
        

    return render(request,'cars/search.html',context)