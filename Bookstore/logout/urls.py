from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.base,name='home'),
    path('home/',views.base,name='home'),
    path('checklogin/',views.checklogin,name="checklogin"),
    path('profile/',views.profile,name='profile'),
    path('addregister/',views.addregister,name="addregister"),
    path('cart/', views.cart, name='cart'),
]