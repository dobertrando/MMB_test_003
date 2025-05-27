from django.urls import path
from . import views

urlpatterns = [
    path('deelnemers/', views.deelnemer, name='deelnemers'),
    path('deelnemers/<int:deelnemer_id>/', views.deelnemer_detail, name='deelnemer_detail'),
    
]