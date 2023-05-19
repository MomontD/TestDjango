from django.db import models

# from django.core.exceptions import ValidationError

# from deposits.models import Deposits
# from loans.models import Loans

from temp.def_for_operations import *


# Вибір валюти для депозитів та позик
select_currency = [
    ('UAH', 'UAH'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('PLN', 'PLN'),  # Польський злотий
    ('CHF', 'CHF'),  # Швейцірські франки
    ('GBP', 'GBP')   # Англійські Фунти
]

class BaseTableForProducts(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=30)    # Назва продукту
    sum = models.FloatField()                 # Сума
    currency = models.CharField(max_length=30, blank="Enter your choice", choices=select_currency)    # Вибір валюти
    rate = models.FloatField()                # Відсоткова ставка
    period = models.IntegerField(null=True, blank=True) # Період в міс.
    start_date = models.DateField()           # Дата початку
    end_date = models.DateField()             # Дата завершення


class BaseTableForIndicators(models.Model):
    class Meta:
        abstract = True

    dayily_profit = models.FloatField()       # Денний дохід
    month_profit = models.FloatField()        # Місячний дохід
    year_profit = models.FloatField()         # Річний дохід
    total_profit = models.FloatField()        # Загальний дохід