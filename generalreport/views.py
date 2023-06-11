from django.shortcuts import render

from datetime import date

from utils.generalreport.gen_rep_func import calc_investment_sum

from deposits.models import Deposits
from loans.models import Loans
from governments.models import Governments


def general_report(request):

    deposits_sum = calc_investment_sum(Deposits)
    governments_sum = calc_investment_sum(Governments)
    loans_sum = calc_investment_sum(Loans)

    capital = round((deposits_sum + governments_sum + loans_sum), 2)

    return render(request, 'generalreport/generalreport.html', {'deposits_sum': deposits_sum,
                                                                'governments_sum': governments_sum,
                                                                'loans_sum': loans_sum,
                                                                'capital': capital})
