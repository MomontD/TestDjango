from django.urls import path
from . import views

# app_name = 'deposits'

urlpatterns = [
    path('', views.governments, name='governments'),
    path('add_government', views.add_government, name='add_government'),
    path('general_information_on_governments', views.general_information_on_governments, name='general_information_on_governments'),
    path('governments/add_schedule/<int:id>/', views.add_schedule, name='add_schedule'),
    # path('terminate_deposits', views.terminate_deposits, name='terminate_deposits'),
    path('delete_governments', views.delete_governments, name='delete_governments'),
]