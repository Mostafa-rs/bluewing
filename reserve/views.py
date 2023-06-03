import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order, ItemOrder
from .models import *


# Create your views here.

def reserve_details(request):
    if request.user.is_authenticated:
        times = get_object_or_404(Times, user_id=request.user.id)
    else:
        times = Times.objects.get(session_key=request.session.session_key)
    cars = Car.objects.get(id=times.car.id)
    return render(request, 'auth/reserve.html', {'times': times, 'cars': cars})


@login_required(login_url='accounts:login')
def add_reserve(request, id):
    session_key = request.session.get('s_key')
    car = Car.objects.get(id=id)
    if Times.objects.filter(session_key=session_key).exists():
        time = Times.objects.get(session_key=session_key)
    elif Times.objects.filter(user_id=request.user.id).exists():
        time = Times.objects.get(user_id=request.user.id)
    else:
        time = Times.objects.create(user=request.user, session_key=None,
                                    pickup_date=datetime.datetime.now().date() + datetime.timedelta(days=1),
                                    pickup_time=datetime.datetime.now().time(),
                                    return_date=datetime.datetime.now().date() + datetime.timedelta(days=3),
                                    return_time=datetime.datetime.now().time(),
                                    )
    time.car = car
    time.user = request.user
    time.save()
    if session_key:
        del request.session['s_key']
    return redirect('reserve:reserve_details')


def next_level(request):
    pickup_loc = request.POST.get('pickup_location_category')
    print(pickup_loc)
    pickup_date = request.POST.get('pickup_date')
    pickup_time = request.POST.get('pickup_time')
    return_date = request.POST.get('return_date')
    return_time = request.POST.get('return_time')
    return_loc = request.POST.get('return_location_category')
    if pickup_loc == 'doorsteps':
        pickup_loc = request.POST.get('user_address')
    elif pickup_loc == 'airport':
        pickup_loc = request.POST.get('p_terminal')
    if return_loc == 'doorsteps':
        return_loc = request.POST.get('return_user_address')
    elif return_loc == 'rentalhub':
        return_loc = 'Rental Hub'
    elif return_loc == 'airport':
        return_loc = request.POST.get('d_terminal')
    pickup_extra = request.POST.get('pickup_extra')
    dropoff_extra = request.POST.get('dropoff_extra')
    babyseat_extra = request.POST.get('babyseat_extra')
    year1_extra = request.POST.get('year1_extra')
    driver_extra = request.POST.get('driver_extra')
    cdw_extra = request.POST.get('cdw_extra')
    full_pay = True if request.POST.get('full_pay') else False
    if full_pay:
        now_pay = request.POST.get('paid_amount')
        total_cost = request.POST.get('paid_amount')
        later_pay = 0
    else:
        now_pay = request.POST.get('now_paid_amount')
        later_pay = request.POST.get('later_paid_amount')
        total_cost = request.POST.get('paid_amount')

    if Order.objects.filter(user=request.user).exists():
        order = Order.objects.get(user=request.user)
        order.driving_license_back_image = None
        order.driving_license_front_image = None
        order.passport_back_image = None
        order.passport_front_image = None
        order.date_of_birth = None
        order.city = None
        order.nationality = None
        order.phone = None
        order.f_name = None
        order.l_name = None
        order.save()
    else:
        order = Order.objects.create(user=request.user)


    if ItemOrder.objects.filter(user=request.user, order=order, car_id=request.POST.get('car_id')).exists():
        item_order = ItemOrder.objects.get(order=order, user=request.user, car_id=request.POST.get('car_id'))
    else:
        item_order = ItemOrder.objects.create(order=order, user=request.user, car_id=request.POST.get('car_id'))
    item_order.now_pay_cost = now_pay
    item_order.later_pay_cost = later_pay
    item_order.total_cost = total_cost
    item_order.pickup_location = pickup_loc
    item_order.pickup_time = pickup_time
    item_order.pickup_date = pickup_date
    item_order.return_location = return_loc
    item_order.return_time = return_time
    item_order.return_date = return_date
    item_order.full_pay = full_pay
    item_order.save()

    if pickup_extra:
        item_order.extra_services.add(Extras.objects.get(name__icontains='pick'))
    else:
        if item_order.extra_services.filter(id=Extras.objects.get(name__icontains='pick').id).exists():
            item_order.extra_services.remove(Extras.objects.get(name__icontains='pick'))
    if dropoff_extra:
        item_order.extra_services.add(Extras.objects.get(name__icontains='drop'))
    else:
        if item_order.extra_services.filter(id=Extras.objects.get(name__icontains='drop').id).exists():
            item_order.extra_services.remove(Extras.objects.get(name__icontains='drop'))
    if babyseat_extra:
        item_order.extra_services.add(Extras.objects.get(name__contains='baby'))
    else:
        if item_order.extra_services.filter(id=Extras.objects.get(name__icontains='baby').id).exists():
            item_order.extra_services.remove(Extras.objects.get(name__icontains='baby'))
    if year1_extra:
        item_order.extra_services.add(Extras.objects.get(name__contains='year'))
    else:
        if item_order.extra_services.filter(id=Extras.objects.get(name__icontains='year').id).exists():
            item_order.extra_services.remove(Extras.objects.get(name__icontains='year'))
    if driver_extra:
        item_order.extra_services.add(Extras.objects.get(name__contains='driver'))
    else:
        if item_order.extra_services.filter(id=Extras.objects.get(name__icontains='driver').id).exists():
            item_order.extra_services.remove(Extras.objects.get(name__icontains='driver'))
    if cdw_extra:
        item_order.extra_services.add(Extras.objects.get(name__contains='cdw'))
    else:
        if item_order.extra_services.filter(id=Extras.objects.get(name__icontains='cdw').id).exists():
            item_order.extra_services.remove(Extras.objects.get(name__icontains='cdw'))

    return redirect('order:order_details')
