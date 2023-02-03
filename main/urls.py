from django.urls import path
from . import views

urlpatterns = [
    path('',views.printhello),
    #path('about ',views.about)
]