from django.urls import path
from . import views
import include

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    #path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('politicas/', views.politicas, name="politicas"),
    path('sample/', views.sample, name="sample"),
#    path('organigrama/', views.organigrama, name="organigrama"),
]
