from django.urls import path

from . import views

app_name = 'reserve'
urlpatterns = [
    path('', views.reserve_details, name='reserve_details'),
    path('add/<int:id>/', views.add_reserve, name='add_reserve'),
    path('next/', views.next_level, name='next_level'),

]
