from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    # path('expenses',   views.expenses,    name='expenses'),
    # path('operations',views.operations,  name='operations'),
    path('analitics',  views.analitics,  name ='analitics'),
    # path('basereport', views.basereport, name ='basereport')
]