# from operations.views import *
from operations.forms import *

calc_sum_all_deposits=0
average_rate_from_deposits=0
amount = 0
array_of_sum_month = []
income_from_deposits = 0
deposit_data = deposit.objects.all()

for element in deposit_data :
    calc_sum_all_deposits += element.deposit_sum
    average_rate_from_deposits += element.deposit_rate
    array_of_sum_month.append(element.deposit_sum*(element.deposit_rate/100)/element.deposit_period)
    income_from_deposits += element.deposit_sum*(element.deposit_rate/100)* (element.deposit_period/12)
    # income_from_deposits = Основна сума * Ставка * Період часу/12
    amount += 1

average_rate = average_rate_from_deposits/amount # Визначення середнього % по депозитам
average_month_income = round(sum(array_of_sum_month),2) # обр. місячний дохід по депозитам
income_from_deposits = round(income_from_deposits)

