from django.db.models import Sum

from deposits.models import Deposits, DepositsIndicators
from loans.models import Loans
from governments.models import Governments, GovernmentIndicators

from datetime import date

def calc_investment_sum(investment):
    # Виятгуємо поле 'sum' з таблиці Deposits,Governments, Loans в залежності що отримаємо на вході.
    # Вибираємо з БД АКТУАЛЬНІ записи - filter(end_date__gt=date.today()
    # Одразу його сумуємо за допомогою агркгатної ф-ї aggregate() та Sum
    # Отримуємо словник з сумою {'deposits_sum': 950300.0}
    # Якщо записи в БД будуть відсутні , отримаємо {'deposits_sum': None}
    dict_investment_sum = investment.objects.filter(end_date__gt=date.today()).aggregate(investment_sum=Sum('sum'))
    # Зі словника {'deposits_sum': 950300.0} забираємо значення 950300.0
    # Якщо записи будуть відсутні і ми отримаємо {'deposits_sum': None} тоді зберігаємо '0'
    investment_sum = dict_investment_sum['investment_sum'] if dict_investment_sum['investment_sum'] is not None else 0

    return round(investment_sum, 2)

def calc_investment_profit(investment_list):
    # Отримуємо на вхід список відфільтрованих обєктів (актуальна дата) з таблиць Deposits або Governments або Loans
    # В залежності що буде на вході
    # <QuerySet [<Deposits: Deposits object (8)>]>
    # АБО
    # <QuerySet [<Governments: Governments object (43)>, <Governments: Governments object (45)>]>
    # АБО
    # <QuerySet [<Loans: Loans object (4)>, <Loans: Loans object (5)>]>
    print(investment_list)

    investment_profit = 0

    # Проганяємо кожен елемент списку та перевіряємо його приналежність до Deposits або Governments або Loans
    # Ця функція універсальна , викликається як для Deposits або Governments або Loans , тому необхідна перевірка кому
    #  належить обєкт, встановлюємо звязок з відповідною таблицею indicators і сумуємо колонку total_profits
    for investment in investment_list:
        if isinstance(investment_list.first(), Deposits):
            deposit_indicators = investment.deposits_indicators.get()
            investment_profit += deposit_indicators.total_profit

        if isinstance(investment_list.first(), Governments):
            government_indicators = investment.governments_indicators.get()
            investment_profit += government_indicators.total_profit

        if isinstance(investment_list.first(), Loans):
            loan_indicators = investment.loans_indicators.get()
            investment_profit += loan_indicators.total_profit

    investment_profit = investment_profit if investment_profit is not None else 0

    return round(investment_profit, 2)

    # if isinstance(investment_list.first(), Governments):
    #     for investment in investment_list:
    #         # gov_id = investment.id
    #         # investment_values = GovernmentIndicators.objects.get(government_id= investment.id)
    #         government_indicators = investment.governments_indicators.get()