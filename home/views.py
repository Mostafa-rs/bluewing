from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.db.models import Q, Max, Min
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from .filters import CarsFilter
from .forms import *
from .models import *


# home_view


# Create your views here.

# def home_view(request):
#     query_times = Times.objects.annotate(
#         duration=ExpressionWrapper(F('return_date') - F('pickup_date'),
#                                    output_field=DurationField()))
#     context = {"query_times": query_times}
#     return render(request, "auth/homeview.html", context)


def home(request):
    category = Category.objects.filter(sub_cat=False)
    # currency = request.get('http://api.backino.net/nerkhapi/api/YOUR_API_CODE/currency/')
    # car = get_object_or_404(Car, id=id)
    cars = Car.objects.all()
    times = Times.objects.all()
    return render(request, 'auth/home.html', {'category': category, 'cars': cars, 'times': times})


def our_services(request):
    return render(request, 'auth/our_services.html')


def about_us(request):
    return render(request, 'auth/about_us.html')


def all_cars(request, slug=None, id=None):
    cars = Car.objects.all()
    min = Car.objects.aggregate(unit_price=Min('unit_price'))
    min_price = int(min['unit_price'])
    max = Car.objects.aggregate(unit_price=Max('unit_price'))
    max_price = int(max['unit_price'])

    filter = CarsFilter(request.GET, queryset=cars)
    cars = filter.qs
    form = SearchForm()
    times = Times.objects.all()
    paginator = Paginator(cars, 9)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    # currency = request.get('http://api.backino.net/nerkhapi/api/YOUR_API_CODE/currency/')

    category = Category.objects.filter(sub_cat=False)
    if slug and id:
        data = Category.objects.get(slug=slug, id=id)
        cars = cars.filter(category=data)
    return render(request, 'auth/cars.html',
                  {'cars': page_obj, 'category': category, 'form': form, 'times': times, 'filter': filter,
                   'min_price': min_price, 'max_price': max_price})


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    images = Images.objects.filter(car_id=id)
    cars = Car.objects.all()
    category = Category.objects.filter(sub_cat=False)
    similar = car.tags.similar_objects()[:4]

    is_like = False
    if car.like.filter(id=request.user.id).exists():
        is_like = True

    is_dislike = False
    if car.dislike.filter(id=request.user.id).exists():
        is_dislike = True
    context = {'car': car, 'category': category, 'similar': similar, 'cars': cars, 'is_like': is_like,
               'is_dislike': is_dislike, 'images': images}
    return render(request, 'auth/details.html', context)


@login_required(login_url='accounts:login')
def car_like(request, id):
    url = request.META.get('HTTP_REFERER')
    car = get_object_or_404(Car, id=id)
    if car.like.filter(id=request.user.id).exists():
        car.like.remove(request.user)
    else:
        if car.dislike.filter(id=request.user.id).exists():
            car.dislike.remove(request.user)
            car.like.add(request.user)
        else:
            car.like.add(request.user)
    return redirect(url)


@login_required(login_url='accounts:login')
def car_dislike(request, id):
    url = request.META.get('HTTP_REFERER')
    car = get_object_or_404(Car, id=id)
    if car.dislike.filter(id=request.user.id).exists():
        car.dislike.remove(request.user)
    else:
        if car.like.filter(id=request.user.id).exists():
            car.like.remove(request.user)
            car.dislike.add(request.user)
        else:
            car.dislike.add(request.user)
    return redirect(url)


def car_search(request):
    cars = Car.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            if data.isdigit():
                cars = cars.filter(Q(unit_price__lte=data))
            else:
                cars = cars.filter(Q(name__icontains=data))
            return render(request, 'auth/cars.html', {'cars': cars, 'form': form})


def find_car(request):
    cars = get_list_or_404(Car)
    if request.method == 'POST':
        form = FindCarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if request.user.is_authenticated:
                if Times.objects.filter(user_id=request.user.id, session_key=None).exists():
                    Times.objects.filter(user_id=request.user.id, session_key=None).delete()
                user_time = Times.objects.create(user_id=request.user.id, session_key=None,
                                                 pickup_time=data['pickup_time'],
                                                 pickup_date=data['pickup_date'], return_date=data['return_date'],
                                                 return_time=data['return_time'])
            else:
                if not request.session.session_key:
                    request.session.create()
                if Times.objects.filter(user_id=None, session_key=request.session.session_key).exists():
                    Times.objects.filter(user_id=None, session_key=request.session.session_key).delete()
                user_time = Times.objects.create(user_id=None, session_key=request.session.session_key,
                                                 pickup_time=data['pickup_time'],
                                                 pickup_date=data['pickup_date'], return_date=data['return_date'],
                                                 return_time=data['return_time'])
        # print(type(user_time.duration))
    #     if request.user.is_authenticated:
    #         cars = get_object_or_404(Car, id=id)
    #         user_car = Times.objects.filter(user_id=request.user.id, session_key=None,
    #                                         cars_id=cars.id)
    #         if user_car.exists():
    #             user_car.delete()
    #     else:
    #         if not request.session.session_key:
    #             request.session.create()
    #         form = FindCarForm(request.POST)
    #         if form.is_valid():
    #             cars = get_object_or_404(Car, id=id)
    #             data = form.cleaned_data
    #             datetime = Times.objects.create(pickup_date=data['pickup_date'], pickup_time=data['pickup_time'],
    #                                             return_date=data['return_date'], return_time=data['return_time'],
    #                                             user_id=request.user.id, session_key=request.session.session_key,
    #                                             cars_id=cars.id)
    #             datetime.save()
    #             return redirect('home:cars')
    # else:
    #     form = FindCarForm(request.POST)

    return render(request, 'auth/cars.html', {'user_time': user_time, 'cars': cars})


def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        name = request.POST['name']
        msg = request.POST['message']
        body = subject + '\n' + name + '\n' + email + '\n' + msg
        form = EmailMessage(
            'contact form',
            body,
            'test',
            ('ddeutschule@gmail.com',),

        )
        form.send(fail_silently=False)

    return render(request, 'auth/contact.html')
