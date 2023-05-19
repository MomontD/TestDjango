from django.shortcuts import render, redirect

from loans.models import Loans
from utils.general.general_functions import grouping, calculate_indicators

from loans.forms import add_loanForm

from datetime import date, datetime


def loans(request):
    return render(request, '')


def general_information_on_loans(request):

    # Вибираємо з бази ВСІ активні позики та групуємо їх по валюті
    active_loans = Loans.objects.filter(end_date__gt=date.today())
    grouped_active_loans = grouping(active_loans)

    # Вибираємо з бази ВСІ позики в архіві та групуємо їх по валюті
    loans_in_archive = Loans.objects.filter(end_date__lt=date.today())
    grouped_archive_loans = grouping(loans_in_archive)

    if grouped_active_loans != 'list is empty':
        # передаємо дод. параметр 'deposits' щоб ф-я знала з яким обєктом працює і яку таблицю з індикаторами витягувати
        report_active_loans = calculate_indicators('loans', grouped_active_loans)
    else:
        report_active_loans = grouped_active_loans  # поверне 'list is empty'

    if grouped_archive_loans != 'list is empty':
        # передаємо дод. параметр 'deposits' щоб ф-я знала з яким обєктом працює і яку таблицю з індикаторами витягувати
        report_archive_loans = calculate_indicators('loans', grouped_archive_loans)
    else:
        report_archive_loans = grouped_archive_loans  # поверне 'list is empty'

    return render(request, 'loans/general_information_on_loans.html',
                  {'grouped_active_loans': grouped_active_loans,
                   'grouped_archive_loans': grouped_archive_loans,
                   # Дані для таблиці з активними депозитами
                   'report_active_loans': report_active_loans,
                   # Дані для таблиці з архівними депозитами
                   'report_archive_loans': report_archive_loans
                   })


def add_loan(request):
    error = ''
    if request.method == "POST":
        form = add_loanForm(request.POST)
        # Поле period згідно базової моделі може бути NULL, але для депозитів і позик - це не підходить, тому робимо
        # додаткову перевірку на заповненість поля period.
        # тільки якщо заповнене поле period та форма пройшла валідацію - відбувається запис в БД
        if form.is_valid() and form.cleaned_data.get('period'):
            form.save()
            form.save()
            return redirect('operations')
        else:
            error = 'Data not accepted! Invalid data in form!'

    form = add_loanForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'loans/add_loan.html', data)


def delete_loans(request):
    error_delete = ''
    successful_operation = ''
    if request.method == 'POST':
        selected_loans = request.POST.getlist('selected_loans')
        if selected_loans :
            Loans.objects.filter(id__in=selected_loans).delete()
            successful_operation = 'The loan has been successfully deleted'
        else:
            error_delete = 'You have not selected a loan!'

    active_loans = Loans.objects.filter(end_date__gt=date.today())
    loans_in_archive = Loans.objects.filter(end_date__lt=date.today())

    return render(request, 'loans/delete_loans.html', {'active_loans': active_loans,
                                                       'loans_in_archive': loans_in_archive,
                                                       'error_delete': error_delete,
                                                       'successful_operation': successful_operation
                                                       })
