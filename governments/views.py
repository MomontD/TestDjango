from django.shortcuts import render, redirect

from governments.forms import add_governmentForm, AddPaymentSchedule

from governments.models import *

from utils.general.general_functions import grouping, calculate_indicators

from utils.governments.gov_func import forming_period_list


def governments(request):
    return render(request, '')


def add_government(request):
    error = ''
    if request.method == "POST":
        form = add_governmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general_information_on_governments')
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
    active_governments = Governments.objects.filter(end_date__gt=date.today()).order_by('start_date')
    grouped_active_governments = grouping(active_governments)

    # Вибираємо з бази ВСІ ОВДП в архіві та групуємо їх по валюті
    governments_in_archive = Governments.objects.filter(end_date__lt=date.today()).order_by('end_date')
    grouped_archive_governments = grouping(governments_in_archive)

    if grouped_active_governments != 'list is empty':
        # передаємо дод. параметр 'governments' щоб ф-я знала з яким обєктом працює і яку таблицю з індикаторами витягувати
        report_active_governments = calculate_indicators('governments', grouped_active_governments)
    else:
        report_active_governments = grouped_active_governments  # поверне 'list is empty'

    if grouped_archive_governments != 'list is empty':
        # передаємо дод. параметр 'governments' щоб ф-я знала з яким обєктом працює і яку таблицю з індикаторами витягувати
        report_archive_governments = calculate_indicators('governments', grouped_archive_governments)
    else:
        report_archive_governments = grouped_archive_governments  # поверне 'list is empty'

    return render(request, 'governments/general_information_on_governments.html',
                  {'active_governments': active_governments,
                   'archive_governments': governments_in_archive,
                   # Дані для таблиці з активними депозитами
                   'report_active_governments': report_active_governments,
                   # Дані для таблиці з архівними депозитами
                   'report_archive_governments': report_archive_governments
                   })

def payments_schedule(request):
    # Витягуємо з таблиці оплат всі оплати + відфіотровуємо по даті (актуальні) + сортуємо по зростанню
    payments_schedule = PaymentSchedule.objects.filter(payment_date__gt=date.today()).order_by('payment_date')
    # За допомогою forming_list_of_years отримуємо список років [2022,2023,2024]
    period_list = forming_period_list(payments_schedule)
    print(period_list)
    return render(request, 'governments/payments_schedule.html',{'period_list': period_list,
                                                                 'payments_schedule': payments_schedule
                                                                 })

def government_details(request, government_id):

    government = Governments.objects.get(id=government_id)

    return render(request, 'governments/government_details.html', {'government': government})


def add_schedule(request, government_id):

    if request.method == "POST":
        # Якщо ми нажали кнопку name="submit_btn" зберігаємо дані в БД і повертаємось до повторного введення даних
        if 'submit_btn' in request.POST:
            form = AddPaymentSchedule(request.POST)
            if form.is_valid():
                # Присвоюємо формі ID ОВДП до якого будем додавати графік виплат
                form.instance.government_id = government_id
                # Зберігаємо форму
                form.save()
                return redirect('add_schedule', government_id=government_id)

        # Відміна видалення графіку оплат
        if 'cencel-delete-payments-schedule' in request.POST:
            return redirect('add_schedule', government_id=government_id)

        # Видалення графіку оплат конкретного ОВДП
        if 'btn-confirm-delete-payments-schedule' in request.POST:
            # government_payments = PaymentSchedule.objects.filter(government_id=government_id)
            # government_payments.delete()
            PaymentSchedule.objects.filter(government_id=government_id).delete()

    data_payment_schedule = PaymentSchedule.objects.filter(government_id=government_id)
    government = Governments.objects.get(id=government_id)
    form = AddPaymentSchedule()
    data = {
        'form': form,
        'government': government,
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