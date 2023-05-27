from django.shortcuts import render, redirect

from governments.forms import add_governmentForm

from datetime import date, datetime

from governments.models import *


def governments(request):
    return render(request, '')


def add_government(request):
    error = ''
    if request.method == "POST":
        form = add_governmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operations')
        else:
            error = 'Data not accepted! Invalid data in form!'

    form = add_governmentForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'governments/add_government.html', data)


def general_information_on_governments(request):

    # Вибираємо з бази ВСІ активні ОВДП та групуємо їх по валюті
    active_governments = Governments.objects.filter(end_date__gt=date.today())
    extended_indicators = GovernmentExtendedIndicators.objects.all()

    # Вибираємо з бази ВСІ ОВДП в архіві та групуємо їх по валюті
    governments_in_archive = Governments.objects.filter(end_date__lt=date.today())


    return render(request, 'governments/general_information_on_governments.html',
                  {'active_governments': active_governments,
                   'extended_indicators': extended_indicators,
                   'archive_governments': governments_in_archive,
                   # # Дані для таблиці з активними депозитами
                   # 'report_active_deposits': report_active_deposits,
                   # # Дані для таблиці з архівними депозитами
                   # 'report_archive_deposits': report_archive_deposits
                   })

def delete_governments(request):
    error_delete_government = ''
    successful_operation_delete_government = ''
    if request.method == 'POST':
        selected_governments = request.POST.getlist('selected_governments')
        if selected_governments :
            Governments.objects.filter(id__in=selected_governments).delete()
            successful_operation_delete_government = 'The government(s) has been successfully deleted'
        else:
            error_delete_government = 'You have not selected a government(s)!'

    active_governments = Governments.objects.filter(end_date__gt=date.today())
    governments_in_archive = Governments.objects.filter(end_date__lt=date.today())

    return render(request, 'governments/delete_governments.html',
                                    {'active_governments': active_governments,
                                     'governments_in_archive': governments_in_archive,
                                     'error_delete_government': error_delete_government,
                                     'successful_operation_delete_government': successful_operation_delete_government
                                     })