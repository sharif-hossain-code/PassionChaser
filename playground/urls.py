from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('service/', views.service_page, name='service'),
]
