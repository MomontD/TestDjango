from django.urls import path
from . import views

# app_name = 'deposits'

urlpatterns = [
    path('', views.deposits, name='deposits'),
    path('add_deposit', views.add_deposit, name='add_deposit'),
    path('general_information_on_deposits', views.general_information_on_deposits, name='general_information_on_deposits'),
    path('add_to_deposit', views.add_to_deposit, name='add_to_deposit'),
    path('terminate_deposits', views.terminate_deposits, name='terminate_deposits'),
    path('delete_deposits', views.delete_deposits, name='delete_deposits'),
]
