from django.urls import path
from . import views


urlpatterns = [
    path('', views.loans, name='loans'),
    path('add_loan', views.add_loan, name='add_loan'),
    path('general_information_on_loans', views.general_information_on_loans, name='general_information_on_loans'),
    path('delete_loans', views.delete_loans, name='delete_loans'),
]
