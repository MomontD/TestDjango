# from operations.views import *
from operations.forms import *

deposit_data = deposit.objects.all()
loans_data = loan.objects.all()

# Операції для депозитів
calc_sum_all_deposits = 0
average_rate_from_deposits = 0
array_of_sum_month =[]
income_from_deposits = 0
amount=0

for element in deposit_data :
    calc_sum_all_deposits += element.deposit_sum
    average_rate_from_deposits += element.deposit_rate
    # Визначення місячного доходу по депозитам
    # Записуємо в масив місячний дохід по кожному депозиту і потім сумуємо значення
    # Формула : місячний дохід = сума депозиту * ставка % * період (12міс.-1, 6міс.-0,5, 3 міс. - 0,25) - тут ми
    # дізнаємось загальний дохід від депозиту , далі ділимо на період 12,6,3міс.
    # Приклад : 100 000 грн * 18% * 1 = 18 0000 грн / 12міс. = 1 500 грн в міс.
    array_of_sum_month.append(element.deposit_sum*(element.deposit_rate/100)*(element.deposit_period/12)/element.deposit_period)
    # Визначення загального доходу по депозитам
    # Формула : Основна сума * Ставка * Період часу/12
    income_from_deposits += (element.deposit_sum*(element.deposit_rate/100))* (element.deposit_period/12)
    amount += 1

average_rate_from_deposits = average_rate_from_deposits/amount # Визначення середнього % по депозитам
average_month_income = round(sum(array_of_sum_month),2) # обр. місячний дохід по депозитам
income_from_deposits = round(income_from_deposits)

# Операції для Позик :
# for element in loans_data :
#     calc_sum_all_loans += element.debt_sum
#     average_rate_from_deposits += element.deposit_rate
#     # Визначення місячного доходу по депозитам
#     # Записуємо в масив місячний дохід по кожному депозиту і потім сумуємо значення
#     # Формула : місячний дохід = сума депозиту * ставка % * період (12міс.-1, 6міс.-0,5, 3 міс. - 0,25) - тут ми
#     # дізнаємось загальний дохід від депозиту , далі ділимо на період 12,6,3міс.
#     # Приклад : 100 000 грн * 18% * 1 = 18 0000 грн / 12міс. = 1 500 грн в міс.
#     array_of_sum_month.append(element.deposit_sum*(element.deposit_rate/100)*(element.deposit_period/12)/element.deposit_period)
#     # Визначення загального доходу по депозитам
#     # Формула : Основна сума * Ставка * Період часу/12
#     income_from_deposits += (element.deposit_sum*(element.deposit_rate/100))* (element.deposit_period/12)
#     amount += 1
#
# average_rate_from_deposits = average_rate_from_deposits/amount # Визначення середнього % по депозитам
# average_month_income = round(sum(array_of_sum_month),2) # обр. місячний дохід по депозитам
# income_from_deposits = round(income_from_deposits)