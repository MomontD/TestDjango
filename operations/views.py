from django.shortcuts import render


def operations(request):
    return render (request, 'operations/operations.html')