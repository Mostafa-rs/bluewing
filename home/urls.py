from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    # path('homeview/', views.home_view, name="home_view"),
    path('cars/', views.all_cars, name='cars'),
    path('detail/<int:id>/', views.car_detail, name='detail'),
    path('category/<slug>/<int:id>/', views.all_cars, name='category'),
    path('like/<int:id>/', views.car_like, name='car_like'),
    path('dislike/<int:id>/', views.car_dislike, name='car_dislike'),
    path('search/', views.car_search, name='car_search'),
    path('findcar/', views.find_car, name='find_car'),
    path('contact/', views.contact, name='contact'),
    path('ourServices/', views.our_services, name='our_services'),
    path('aboutUs/', views.about_us, name='about_us'),
]
