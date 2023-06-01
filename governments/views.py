from django.shortcuts import render, redirect

from governments.forms import add_governmentForm, AddPaymentSchedule

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

    # Вибираємо з бази ВСІ ОВДП в архіві та групуємо їх по валюті
    governments_in_archive = Governments.objects.filter(end_date__lt=date.today())


    return render(request, 'governments/general_information_on_governments.html',
                  {'active_governments': active_governments,
                   'archive_governments': governments_in_archive,
                   # # Дані для таблиці з активними депозитами
                   # 'report_active_deposits': report_active_deposits,
                   # # Дані для таблиці з архівними депозитами
                   # 'report_archive_deposits': report_archive_deposits
                   })


def add_schedule(request, id):

    if request.method == "POST":
        # Якщо ми нажали кнопку name="submit_btn" зберігаємо дані в БД і повертаємось до повторного введення даних
        if 'submit_btn' in request.POST:
            form = AddPaymentSchedule(request.POST)
            if form.is_valid():
                # Присвоюємо формі ID ОВДП до якого будем додавати графік виплат
                form.instance.government_id = id
                # Зберігаємо форму
                form.save()
                return redirect('add_schedule', id=id)

        # # Якщо ми нажали кнопку name="submit_and_redirect" повертаємось на сторінку з відобрж. ОВДП
        elif 'submit_and_redirect' in request.POST:
            return redirect('general_information_on_governments')

    data_payment_schedule = PaymentSchedule.objects.filter(government_id=id)
    form = AddPaymentSchedule()
    data = {
        'form': form,
        'government_id': id,
        'data_payment_schedule': data_payment_schedule,
    }

    return render(request, 'governments/add_schedule.html', data)


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