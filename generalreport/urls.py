from django.urls import path
from . import views

urlpatterns = [
    path('', views.general_report, name='general_report'),
]