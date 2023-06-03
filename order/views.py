from django.shortcuts import render, redirect, get_object_or_404

from .models import *


# Create your views here.

def order_details(request):
    if request.method == 'POST':
        order = get_object_or_404(Order, user=request.user)
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            update_order = form.save(commit=False)
            update_order.nationality = request.POST['id_nationality']
            update_order.save()
            return redirect('home:home')
    else:
        form = OrderForm()
    return render(request,'auth/order.html', {'form': form})


