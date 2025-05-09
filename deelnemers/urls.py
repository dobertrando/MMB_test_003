from django.urls import path
from . import views

urlpatterns = [
    path('deelnemers/', views.deelnemer, name='deelnemers'),
]