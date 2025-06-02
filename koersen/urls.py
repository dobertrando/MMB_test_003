from django.urls import path
from . import views

urlpatterns = [
    path('koersen/', views.koers, name='koersen'),
    path('koersen/<int:koers_id>/', views.koers_detail, name='koers_detail'),
    
    
]