# from operations.views import *
# from operations.forms import *

def calculate_data (incoming_data) :
    counter = 0       # лічильник ітерацій циклу / необхідний для обрахування середнього %
    calc_sum = 0      # Обрахунок загальної суми депозитів , позик , ОВДП
    average_rate = 0  # Середній відсоток по депозитам , позикам , ОВДП
    total_profit = 0  # Загальний дохід з депозитам , позикам , ОВДП
    array_of_monthly_profit =[] # масив з місячних доходів з кожного депозиту , позики

    for element in incoming_data :
        calc_sum += element.sum
        average_rate += element.rate
        array_of_monthly_profit.append(element.sum*(element.rate/100)*(element.period/12)/element.period)
        total_profit += (element.sum*(element.rate/100))* (element.period/12)
        counter += 1

    if average_rate != 0 :
        average_rate = average_rate/counter                         # Визначення середнього % по депозитам
    total_profit = round(total_profit,2)
    array_of_monthly_profit = round(sum(array_of_monthly_profit),2) # обр. місячний дохід по депозитам

    return [calc_sum,total_profit,average_rate,array_of_monthly_profit]

# Визначення місячного доходу по депозитам :
#  - Записуємо в масив місячний дохід по кожному депозиту і потім сумуємо значення
#  - Формула : місячний дохід = сума депозиту * ставка % * період (12міс.-1, 6міс.-0,5, 3 міс. - 0,25) - тут ми
#    дізнаємось загальний дохід від депозиту , далі ділимо на період 12,6,3міс.
#  - Приклад : 100 000 грн * 18% * 1 = 18 0000 грн / 12міс. = 1 500 грн в міс.
# Визначення загального доходу по депозитам :
# Формула : Основна сума * Ставка * Період часу/12


# # Операції для Позик :
# # for element in loans_data :
# #     calc_sum_all_loans += element.debt_sum
# #     average_rate_from_deposits += element.deposit_rate
# #     # Визначення місячного доходу по депозитам
# #     # Записуємо в масив місячний дохід по кожному депозиту і потім сумуємо значення
# #     # Формула : місячний дохід = сума депозиту * ставка % * період (12міс.-1, 6міс.-0,5, 3 міс. - 0,25) - тут ми
# #     # дізнаємось загальний дохід від депозиту , далі ділимо на період 12,6,3міс.
# #     # Приклад : 100 000 грн * 18% * 1 = 18 0000 грн / 12міс. = 1 500 грн в міс.
# #     array_of_sum_month.append(element.deposit_sum*(element.deposit_rate/100)*(element.deposit_period/12)/element.deposit_period)
# #     # Визначення загального доходу по депозитам
# #     # Формула : Основна сума * Ставка * Період часу/12
# #     income_from_deposits += (element.deposit_sum*(element.deposit_rate/100))* (element.deposit_period/12)
# #     amount += 1
# #
# # average_rate_from_deposits = average_rate_from_deposits/amount # Визначення середнього % по депозитам
# # average_month_income = round(sum(array_of_sum_month),2) # обр. місячний дохід по депозитам
# # income_from_deposits = round(income_from_deposits)