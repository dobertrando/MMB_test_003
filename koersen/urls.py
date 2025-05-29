from django.urls import path
from . import views

urlpatterns = [
    path('koersen/', views.koers, name='koersen'),
    
]