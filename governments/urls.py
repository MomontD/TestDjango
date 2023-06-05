from django.urls import path
from . import views

# app_name = 'deposits'

urlpatterns = [
    path('', views.governments, name='governments'),
    path('add_government', views.add_government, name='add_government'),
    path('general_information_on_governments', views.general_information_on_governments, name='general_information_on_governments'),
    path('add_schedule/<int:government_id>/', views.add_schedule, name='add_schedule'),
    path('government_details/<int:government_id>/', views.government_details, name='government_details'),
    path('payments_schedule', views.payments_schedule, name='payments_schedule'),
    path('delete_governments', views.delete_governments, name='delete_governments'),
]