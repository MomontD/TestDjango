from django.shortcuts import render
from main.static.main.py import test # імпортуємо всі ф-ї з статичного файлу test

# def printhello(request):
#     return render (request,'main/home.html')

def home (request) :
    return render (request, 'main/home.html', test.obj())

# def expenses (request):
#     return render (request, 'main/expenses.html')

# def operations (request) :
#     return render (request, 'main/../operations/templates/operations/operations.html')

def analitics(request) :
    return render (request, 'main/analitics.html')

def basereport(request) :
    return render (request, 'main/../generalreport/templates/generalreport/generalreport.html')

