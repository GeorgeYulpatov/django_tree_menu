from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/team/', views.team, name='team'),
    path('about/history/', views.history, name='history'),
    path('services/', views.services, name='services'),
    path('services/maintenance/', views.maintenance, name='maintenance'),
    path('services/consulting/', views.consulting, name='consulting'),
    path('contact/', views.contact, name='contact'),
]
