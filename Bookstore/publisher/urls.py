from django.urls import path
from .import views
urlpatterns = [
    path('viewdetails/', views.vieworder, name="viewdetails"),
    path('phome/',views.home,name='phome'),
    path('dashboard',views.dashboard,name="dashboard")
    ]