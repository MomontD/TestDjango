from django.shortcuts import render

from utils.generalreport.gen_rep_func import calc_investment_sum, calc_investment_profit, calc_investments_indicators

from datetime import date

from deposits.models import Deposits
from loans.models import Loans
from governments.models import Governments


def general_report(request):

    # Витягуємо суми всіх інвестицій (по одному на кожен вид) => {'deposits_sum': 950300.0} .. {'loans_sum': 950300.0}
    # Актуальні дані!!! з БД - діючі інвестиції, цей фільтр стоїть у ф-ї calc_investment_sum
    deposits_sum = calc_investment_sum(Deposits)
    governments_sum = calc_investment_sum(Governments)
    loans_sum = calc_investment_sum(Loans)

    # Отримуємо суми доходів всіх інвестиціях (по одному на кожен вид)
    deposits_profit = calc_investment_profit(Deposits.objects.filter(end_date__gt=date.today(), currency='UAH'))
    governments_profit = calc_investment_profit(Governments.objects.filter(end_date__gt=date.today(), currency='UAH'))
    loans_profit = calc_investment_profit(Loans.objects.filter(end_date__gt=date.today(), currency='UAH'))

    # Загальна сума всіх інвестицій
    capital = round((deposits_sum + governments_sum + loans_sum), 2)
    # Загальний дохід всіх інвестицій
    total_profit = deposits_profit + governments_profit + loans_profit
    # % дохід/сума
    profit_rate = round((total_profit/capital)*100, 2)

    # Отриуємо дані зі всіх інвестицій таблиць(indicators) для звіту general report (day,moth,year,total profit)
    deposits_data_UAH = Deposits.objects.filter(end_date__gt=date.today(), currency='UAH')
    governments_data_UAH = Governments.objects.filter(end_date__gt=date.today(), currency='UAH')
    loans_data_UAH = Loans.objects.filter(end_date__gt=date.today(), currency='UAH')

    # Обраховуємо по інвестиціям ((депозитам, ОВДП, позикам) суми індикаторів  -  ((дений , міс.,річ)
    # Поваертається список :
    #    sum=dep/bonds/loans        sum=dep/bonds/loans      sum=dep/bonds/loans
    # [{'dayily_profit': 133.48, 'month_profit': 4059.94, 'year_profit': 48719.32},
    day_indicators_UAH, month_indicators_UAH, year_indicators_UAH, sum_indicators_UAH = \
        calc_investments_indicators(deposits_data_UAH, governments_data_UAH, loans_data_UAH)

    investment_profit_indicators = {
        'Dayily profit': day_indicators_UAH,
        'Month profit': month_indicators_UAH,
        'Year profit': year_indicators_UAH,
        # 'sum_indicators_UAH': sum_indicators_UAH
    }

    print(day_indicators_UAH, month_indicators_UAH, year_indicators_UAH, sum_indicators_UAH)

    return render(request, 'generalreport/generalreport.html', {'deposits_sum': deposits_sum,
                                                                'governments_sum': governments_sum,
                                                                'loans_sum': loans_sum,
                                                                'capital': capital,
                                                                'total_profit': total_profit,
                                                                'profit_rate': profit_rate,
                                                                'deposits_profit': deposits_profit,
                                                                'governments_profit': governments_profit,
                                                                'loans_profit': loans_profit,
                                                                'investment_profit_indicators': investment_profit_indicators})

