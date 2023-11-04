from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('lhome/',views.lhome,name='lhome'),
    path('lprofile/',views.profile,name='lprofile'),
    path('lcontact/',views.contact,name='lcontact'),
    path('lcomics/',views.comics,name="lcomics"),
    path('lhp/',views.hp,name="lhp"),
    path('vol1/', views.vol1, name="vol1"),
    path('vol2/', views.vol2, name="vol2"),
    path('vol3/', views.vol3, name="vol3"),
    path('vol4/', views.vol4, name="vol4"),
    path('vol5', views.vol5,name="vol5"),
    path('hvol1/', views.hvol1, name="hvol1"),
    path('hvol2/', views.hvol2, name="hvol2"),
    path('hvol3/', views.hvol3, name="hvol3"),
    path('hvol4/', views.hvol4, name="hvol4"),
    path('hvol5', views.hvol5,name="hvol5"),
    path('checkbook', views.checkbook, name="checkbook"),
    path('form', views.form, name="form"),
path('addpersonal/', views.addpersonal, name="addpersonal"),

path('admin1/', views.admin, name="admin1"),
path('success/', views.success, name="success"),
path('error/', views.error, name="error"),






]