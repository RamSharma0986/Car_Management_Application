from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car/create/', views.car_create, name='car_create'),
    path('car/<int:car_id>/update/', views.car_update, name='car_update'),
    path('car/<int:car_id>/delete/', views.car_delete, name='car_delete'),
]
