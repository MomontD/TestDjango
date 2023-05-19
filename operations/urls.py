from django.urls import path
from . import views

urlpatterns = [
    # Goverments
    path('', views.operations, name='operations'),
    # path('add_government', views.add_government, name='add_government'),
    # Deposits
    # path('deposits/add_deposit', views.add_deposit, name='add_deposit'),
    # path('deposits/general_information_on_deposits', views.general_information_on_deposits, name='general_information_on_deposits'),
    # path('deposits/add_to_deposit', views.add_to_deposit, name='add_to_deposit'),
    # path('deposits/delete_deposits', views.delete_deposits, name='delete_deposits'),
    #Loans
    # path('loans/add_loan', views.add_loan, name='add_loan'),
    # path('loans/general_information_on_loans', views.general_information_on_loans, name='general_information_on_loans'),
    # path('loans/delete_loans', views.delete_loans, name='delete_loans')
]
