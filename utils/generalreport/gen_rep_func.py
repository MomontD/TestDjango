from django.db.models import Sum

from deposits.models import Deposits
from loans.models import Loans
from governments.models import Governments

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


def calc_investments_indicators(deposit_data,governments_data,loans_data):

    def calc_category_indicators(temporary_obj, instance):

        if 'dayily_profit' not in temporary_obj:
            temporary_obj['dayily_profit'] = round(instance.dayily_profit, 2)
        else:
            temporary_obj['dayily_profit'] += round(instance.dayily_profit, 2)

        if 'month_profit' not in temporary_obj:
            temporary_obj['month_profit'] = round(instance.month_profit, 2)
        else:
            temporary_obj['month_profit'] += round(instance.month_profit, 2)

        if 'year_profit' not in temporary_obj:
            temporary_obj['year_profit'] = round(instance.year_profit, 2)
        else:
            temporary_obj['year_profit'] += round(instance.year_profit, 2)

        return temporary_obj

    deposits_values ={}
    governments_values = {}
    loans_values = {}

    day_indicators = {}
    month_indicators = {}
    year_indicators ={}

    keys = ['deposits', 'governments', 'loans']
    for element in [day_indicators, month_indicators, year_indicators]:
        for key in keys:
            if key not in element:
                element[key] = 0


    # Сумуємо індикатори(дений , міс.,річ) показники для кожного виду інвестицій
    # {'dayily_profit': 133.48, 'month_profit': 4059.94, 'year_profit': 48719.32}
    if deposit_data:
        for deposit in deposit_data:
            deposit_indicators = deposit.deposits_indicators.get()
            deposits_values = calc_category_indicators(deposits_values, deposit_indicators)

        day_indicators['deposits'] = round(deposits_values['dayily_profit'], 2)
        month_indicators['deposits'] = round(deposits_values['month_profit'], 2)
        year_indicators['deposits'] = round(deposits_values['year_profit'], 2)

    if governments_data:
        for government in governments_data :
            government_indicators = government.governments_indicators.get()
            governments_values = calc_category_indicators(governments_values, government_indicators)

        day_indicators['governments'] = round(governments_values['dayily_profit'], 2)
        month_indicators['governments'] = round(governments_values['month_profit'], 2)
        year_indicators['governments'] = round(governments_values['year_profit'], 2)

    if loans_data:
        for loan in loans_data:
            loan_indicators = loan.loans_indicators.get()
            loans_values = calc_category_indicators(loans_values, loan_indicators)

        day_indicators['loans'] = round(loans_values['dayily_profit'], 2)
        month_indicators['loans'] = round(loans_values['month_profit'], 2)
        year_indicators['loans'] = round(loans_values['year_profit'], 2)

    # складаємо список з інвестиціями по яких відбулись обрахунки по індикаторам (відсіюємо пусті інвестиції)
    # [{'dayily_profit': 133.48, 'month_profit': 4059.94, 'year_profit': 48719.32} ,
    #  {'dayily_profit': 133.48, 'month_profit': 4059.94, 'year_profit': 48719.32}]
    data_investments = [investment for investment in [deposits_values, governments_values, loans_values] if investment]
    # сумуємо індикатори(дений , міс.,річ) по інвестиціям та додаємо в обєкти
    # {'dayily_profit': 133.48, 'month_profit': 4059.94, 'year_profit': 48719.32}
    day_indicators['summary_profit'] = round(sum(obj.get('dayily_profit') for obj in data_investments), 2)
    month_indicators['summary_profit'] = round(sum(obj.get('month_profit') for obj in data_investments), 2)
    year_indicators['summary_profit'] = round(sum(obj.get('year_profit') for obj in data_investments), 2)

    # повертаємо список з :
    # 1. Обєктами : day_indicators,month_indicators,year_indicators
    #    на кожен період day,month,year =  {'deposits': 133.48, 'governments': 133.48, 'loans': 0}
    # 2. sum_values - просумовані показники по всім інвестиціям :
    #    {'dayily_profit': 903.54, 'month_profit': 27375.52, 'year_profit': 328506.25}
    return [day_indicators,month_indicators,year_indicators]


# sum_values = {
    #     'dayily_profit': round(sum(obj.get('dayily_profit') for obj in data_investments), 2),
    #     'month_profit': round(sum(obj.get('month_profit') for obj in data_investments), 2),
    #     'year_profit': round(sum(obj.get('year_profit') for obj in data_investments), 2)
    # }