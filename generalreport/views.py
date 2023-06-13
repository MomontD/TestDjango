from django.shortcuts import render

from utils.generalreport.gen_rep_func import calc_investment_sum, calc_investment_profit

from datetime import date

from deposits.models import Deposits
from loans.models import Loans
from governments.models import Governments


def general_report(request):

    # Витягуємо суми всіх інвестицій (по одному на кожен вид) => {'deposits_sum': 950300.0} .. {'loans_sum': 950300.0}
    deposits_sum = calc_investment_sum(Deposits)
    governments_sum = calc_investment_sum(Governments)
    loans_sum = calc_investment_sum(Loans)

    # Отримуємо суми доходів всіх інвестиціях (по одному на кожен вид)
    deposits_profit = calc_investment_profit(Deposits.objects.filter(end_date__gt=date.today()))
    governments_profit = calc_investment_profit(Governments.objects.filter(end_date__gt=date.today()))
    loans_profit = calc_investment_profit(Loans.objects.filter(end_date__gt=date.today()))
    print(loans_profit)

    capital = round((deposits_sum + governments_sum + loans_sum), 2)
    total_profit = deposits_profit + governments_profit + loans_profit
    profit_rate = round((total_profit/capital)*100, 2)

    return render(request, 'generalreport/generalreport.html', {'deposits_sum': deposits_sum,
                                                                'governments_sum': governments_sum,
                                                                'loans_sum': loans_sum,
                                                                'capital': capital,
                                                                'total_profit': total_profit,
                                                                'profit_rate': profit_rate,
                                                                'deposits_profit': deposits_profit,
                                                                'governments_profit': governments_profit,
                                                                'loans_profit': loans_profit})
