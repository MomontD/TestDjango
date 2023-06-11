from django.db.models import Sum

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
