from django.shortcuts import render, redirect

from deposits.models import Deposits
from utils.general.general_functions import grouping, calculate_indicators
from utils.deposits.deposit_func import defining_month

from deposits.forms import add_depositForm

from datetime import date, datetime


def deposits(request):
    return render(request, '')


def general_information_on_deposits(request):

    # Вибираємо з бази ВСІ активні депозити та групуємо їх по валюті
    active_deposits = Deposits.objects.filter(end_date__gt=date.today())
    grouped_active_deposits = grouping(active_deposits)

    # Вибираємо з бази ВСІ депозити в архіві та групуємо їх по валюті
    deposits_in_archive = Deposits.objects.filter(end_date__lt=date.today())
    grouped_archive_deposits = grouping(deposits_in_archive)

    if grouped_active_deposits != 'list is empty':
        # передаємо дод. параметр 'deposits' щоб ф-я знала з яким обєктом працює і яку таблицю з індикаторами витягувати
        report_active_deposits = calculate_indicators('deposits', grouped_active_deposits)
    else:
        report_active_deposits = grouped_active_deposits  # поверне 'list is empty'

    if grouped_archive_deposits != 'list is empty':
        # передаємо дод. параметр 'deposits' щоб ф-я знала з яким обєктом працює і яку таблицю з індикаторами витягувати
        report_archive_deposits = calculate_indicators('deposits', grouped_archive_deposits)
    else:
        report_archive_deposits = grouped_archive_deposits  # поверне 'list is empty'

    return render(request, 'deposits/general_information_on_deposits.html',
                  {'grouped_active_deposits': grouped_active_deposits,
                   'grouped_archive_deposits': grouped_archive_deposits,
                   # Дані для таблиці з активними депозитами
                   'report_active_deposits': report_active_deposits,
                   # Дані для таблиці з архівними депозитами
                   'report_archive_deposits': report_archive_deposits
                   })


def add_deposit(request):
    error = ''
    if request.method == "POST":
        form = add_depositForm(request.POST)
        # Поле period згідно базової моделі може бути NULL, але для депозитів і позик - це не підходить, тому робимо
        # додаткову перевірку на заповненість поля period.
        # тільки якщо заповнене поле period та форма пройшла валідацію - відбувається запис в БД
        if form.is_valid() and form.cleaned_data.get('period'):
            form.save()
            return redirect('operations')
        else:
            error = 'Data not accepted! Invalid data in form!'

    form = add_depositForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'deposits/add_deposit.html', data)


def add_to_deposit(request):
    # Фільтруємо депозити з БД - тільки активні(діючі) і в кого статус до поповнення apply
    error = ''
    successful_operation = ''
    if request.method == 'POST':
        add_sum = request.POST.get('data')  # суму на яку поповнюємо депозит беремо з input
        id = request.GET.get('id')          # id депозиту беремо з форми form ( id передається у форму при формуванні таблиці)

        try:
            add_to_deposit = Deposits.objects.get(id=id)
            add_to_deposit.sum += int(add_sum)
            add_to_deposit.save()
            successful_operation = 'The deposit has been successfully replenished!'
        except:
            error = 'Data not accepted! Entered data is not numeric ! Please enter a numeric value'

    deposits_to_add = Deposits.objects.filter(end_date__gt=date.today(), add_deposit="apply")

    return render(request, 'deposits/add_to_deposit.html', {'deposits_to_add': deposits_to_add,
                                                            'error': error,
                                                            'successful_operation': successful_operation})


def terminate_deposits(request):
    error = ''
    successful_operation = ''
    if request.method == 'POST':
        terminate_date = request.POST.get('terminate_date')  # дата розірванням - беремо з input name='terminate_date'
        terminate_rate = request.POST.get('terminate_rate')  # % розірвання - беремо з input name='terminate_rate'
        id = request.GET.get('id')          # id депозиту беремо з форми form ( id передається у форму при формуванні таблиці)

        try:
            terminate_date = datetime.strptime(terminate_date, '%Y-%m-%d').date() # при вводі дати має тип str , перетворюємо на обєкт дата/ .date - дата без часу
            deposit_to_terminate = Deposits.objects.get(id=id)             # витягуємо депозит по id який передаємо по url з форми
            deposit_to_terminate.end_date = terminate_date                 # присвоюємо кінцевій даті депозиту - дату розірвання договору
            deposit_to_terminate.rate = float(terminate_rate)              # при вводі дати має тип str , перетворюємо на float
            # Ф-я з визначення к-сті місяців, які записуємо в колонку "period", депозиту
            deposit_to_terminate.period = defining_month(deposit_to_terminate,terminate_date)
            deposit_to_terminate.terminate_deposit = 'terminated'
            deposit_to_terminate.save()
            successful_operation = 'The deposit has been successfully terminated!'
        except:
            error = 'Data not accepted! Entered data is not valid ! Please enter a correct data!'

    # Фільтруємо депозити з БД - тільки активні(діючі) і в кого статус з достроковим розірванням = apply
    deposits_to_terminate = Deposits.objects.filter(end_date__gt=date.today(), terminate_deposit="apply")

    return render (request, 'deposits/terminate_deposits.html', {'deposits_to_terminate': deposits_to_terminate,
                                                                 'error': error,
                                                                 'successful_operation': successful_operation})


def delete_deposits(request):
    error_delete_deposit = ''
    successful_operation_delete_deposit = ''
    if request.method == 'POST':
        selected_deposits = request.POST.getlist('selected_deposits')
        if selected_deposits :
            Deposits.objects.filter(id__in=selected_deposits).delete()
            successful_operation_delete_deposit = 'The deposit has been successfully deleted'
        else:
            error_delete_deposit = 'You have not selected a deposit!'

    active_deposits = Deposits.objects.filter(end_date__gt=date.today())
    deposits_in_archive = Deposits.objects.filter(end_date__lt=date.today())

    return render(request, 'deposits/delete_deposits.html', {'active_deposits'     : active_deposits,
                                                             'deposits_in_archive' : deposits_in_archive,
                                                             'error_delete_deposit' : error_delete_deposit,
                                                             'successful_operation_delete_deposit' : successful_operation_delete_deposit
                                                             })