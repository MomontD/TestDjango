from django.db import models
from main.models import BaseTableForProducts, BaseTableForIndicators

select_type_payment = [
    ('coupons payment', 'coupons payment'),
    ('return sum governments', 'return sum governments'),
]

select_type_gv = [
    ('SIM', 'SIM'),
    ('YTM', 'YTM'),
]

# ТАБЛИЦЯ З ОВДП
class Governments(BaseTableForProducts):

    class Meta:
        db_table = 'governments'

    type_gv = models.CharField(max_length=3, blank="Enter your choice", choices=select_type_gv)    # Тип ОВДП = YTM/SIM
    coupons = models.IntegerField()               # Кількість придбаних купонів
    coupons_nominal_cost = models.FloatField()    # Номінальна вартість купона
    coupons_current_cost = models.FloatField()    # Фактична(по якій придбав) купон
    bonds_repayment_nominal = models.FloatField() # Загальна виплата по ОВДП згідно номіналу (купони + %)
    bonds_expenses = models.FloatField()          # Витрати на обслуговування ОВДП


# ТАБЛИЦЯ З ПОКАЗНИКАМИ ОВДП (ДЕННИЙ, МІСЯЧНИЙ, РІЧНИЙ, ЗАГАЛЬНИЙ ДОХОДИ + ФАКТИЧНИЙ %
class GovernmentIndicators(BaseTableForIndicators):

    class Meta:
        db_table = 'governments_indicators'

    current_rate = models.FloatField()            # Фактичний %  = (Загальна сума виплат - суму вкладу ОВДП + дохід/збиток від вартості купону)
    bonds_nominal_cost = models.FloatField()      # Номінальна вартість ОВДП
    bonds_nominal_profit = models.FloatField()    # Номінальний дохід
    coupons_cost_difference = models.FloatField() # Різниця вартості купонів між номінальною і фактичною.
    coupons_current_profit = models.FloatField()  # Різниця вартості купонів (номінальний/фактичний)
    bonds_current_profit = models.FloatField()    # Купонний  дохід/збиток
    government = models.ForeignKey(Governments, on_delete=models.CASCADE, related_name='governments_indicators')


# ТАБЛИЦЯ ГРАФІКОМ ВИПЛАТ КУПОНІВ ТА ПОГАШЕННЯ ОВДП
class PaymentSchedule(models.Model):

    class Meta:
        db_table = 'payments_schedule'

    # Вид виплат - купонний дохід або погашення ОВДП
    payment_type = models.CharField(max_length=30, blank="Enter your choice", choices=select_type_payment)
    payment_date = models.DateField()  # Дата виплати
    payment_sum = models.FloatField()  # Сума виплати
    government = models.ForeignKey(Governments, on_delete=models.CASCADE, related_name='payments_schedule')