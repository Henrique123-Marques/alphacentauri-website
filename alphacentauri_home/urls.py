from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curiosities/', views.curiosities, name='curiosities'),
    path('contact/', views.contact, name='contact'),
]
