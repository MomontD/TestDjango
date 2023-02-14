from django.urls import path
from . import views

urlpatterns = [
    path('',views.operations, name='operations'),
    path('add_data',views.add_data, name='add_data')
]