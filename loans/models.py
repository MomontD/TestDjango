from django.db import models
from main.models import BaseTableForProducts, BaseTableForIndicators

from utils.general.general_functions import calculate_product_indicators

import calendar
from datetime import date



# Необхідна для відхоплювання "сигналів" | будемо ловити момент створення нового депозиту і
from django.db.models.signals import post_save
# Необхідна для відхоплювання "сигналів" | після цього прораховувати його показники+записувати в БД
from django.dispatch import receiver


class Loans(BaseTableForProducts):

    class Meta:
        db_table = 'loans'


class LoansIndicators(BaseTableForIndicators):

    class Meta:
        db_table = 'loans_indicators'

    loan = models.ForeignKey(Loans, on_delete=models.CASCADE, related_name='loans_indicators')


@receiver(post_save, sender=Loans)
def calculate_and_save_product_indicators(instance, created, **kwargs):

    # перевіряємо чи рік високосний (високосний-366 днів)
    is_leap_year = calendar.isleap(instance.end_date.year)
    # контрольна дата 28 Лютого (високосний рік 29 Лютого)
    control_date = date(instance.end_date.year, 2, 28)

    # Якщо термін звершення депозиту у високосний рік більший за 28 Лютого тоді 366 днів інакше 365
    if is_leap_year and instance.end_date > control_date:
        # Обчислюємо показники(доходи - день, міс, рік, загальний) для вхідного продукту
        product_values = calculate_product_indicators(instance, 366)
    else:
        # Обчислюємо показники(доходи - день , міс,рік,загальний) для вхідного продукту
        product_values = calculate_product_indicators(instance, 365)

    # Перевіряємо, чи створено новий продукт
    # При створенні нового продукту created = true, тоді створюється запис у БД
    # Нижче перевіряємо який продукт ми отримали на вході , якщо Deposit у відповідній таблиці і створюється запис
    if created :
        # Створюємо новий запис у таблиці Deposits
        indicators = LoansIndicators.objects.create(
            loan=instance,
            dayily_profit=round(product_values[0], 2),
            month_profit=round(product_values[1], 2),
            year_profit=round(product_values[2], 2),
            total_profit=round(product_values[3], 2)
        )
        # Зберігаємо новий запис
        indicators.save()

    # Якщо created = false , це означає що продукт в БД був і він оновився(додали суму) і перераховуються та
    # записуються нові показники
    else:
        # підєднуємось до таблиці з показниками конкретного депозиту
        indicators = LoansIndicators.objects.get(loan=instance)
        # перезаписуємо показники
        indicators.dayily_profit = round(product_values[0], 2)
        indicators.month_profit = round(product_values[1], 2)
        indicators.year_profit = round(product_values[2], 2)
        indicators.total_profit = round(product_values[3], 2)

        indicators.save()
