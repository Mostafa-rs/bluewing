from django.shortcuts import render

from .models import *


# Create your views here.

def post_list_view(request):
    post_list = Post.objects.all()
    return render(request, 'auth/post_list.html', {'post_list': post_list})
