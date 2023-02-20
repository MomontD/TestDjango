from django.urls import path
from . import views

urlpatterns = [
    path('', views.operations, name='operations'),
    path('add_government', views.add_government, name='add_government'),
    path('add_deposit', views.add_deposit, name='add_deposit'),
    path('add_loan', views.add_loan, name='add_loan'),
    path('active_deposits', views.active_deposits, name='active_deposits')
]
