from django.db import models
from main.models import BaseTableForProducts, BaseTableForIndicators

from utils.governments.gov_func import defining_period, calc_extends_indicators

# Необхідна для відхоплювання "сигналів" | будемо ловити момент створення нового депозиту і
from django.db.models.signals import post_save
# Необхідна для відхоплювання "сигналів" | після цього прораховувати його показники+записувати в БД
from django.dispatch import receiver


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

    government = models.ForeignKey(Governments, on_delete=models.CASCADE,
                                   related_name='governments_indicators')


class GovernmentExtendedIndicators(models.Model):
    class Meta:
        db_table = 'governments_extended_indicators'

    current_rate = models.FloatField()            # Фактичний %  = (Загальна сума виплат - суму вкладу ОВДП + дохід/збиток від вартості купону)
    bonds_nominal_profit = models.FloatField()    # Номінальний дохід
    coupons_cost_difference = models.FloatField() # Різниця вартості купонів між номінальною і фактичною.
    coupons_profit = models.FloatField()          # Купонний дохід/збиток
    government = models.ForeignKey(Governments, on_delete=models.CASCADE,
                                   related_name='governments_extended_indicators')


# ТАБЛИЦЯ ГРАФІКОМ ВИПЛАТ КУПОНІВ ТА ПОГАШЕННЯ ОВДП
class PaymentSchedule(models.Model):

    class Meta:
        db_table = 'payments_schedule'

    # Вид виплат - купонний дохід або погашення ОВДП
    payment_type = models.CharField(max_length=30, blank="Enter your choice", choices=select_type_payment)
    payment_date = models.DateField()  # Дата виплати
    payment_sum = models.FloatField()  # Сума виплати
    government = models.ForeignKey(Governments, on_delete=models.CASCADE, related_name='payments_schedule')



@receiver(post_save, sender=Governments)
def definition_period(instance, **kwargs):
    # Перевіряємо чи поле period null (щоб не було неконтрольованої рекурсії - зациклення)
    # Зациклення виникає коли викликається метод save() - зберегти обєкт в БД, тоді знову спрацьовує @receiver,
    # знову запускає ф-ю з розрахунком періоду і знову метод save() і так по колу ...
    if instance.period is None:
        # викликаємо ф-ю defining_period розрахунку періоду з utils.governments.gov_func
        instance.period = defining_period(instance)
        instance.save()


@receiver(post_save, sender=Governments)
def calculate_and_save_extended_indicators(instance, created, **kwargs):

    if created :

        indicators_tupple = calc_extends_indicators(instance)

        # Створюємо новий запис у таблиці GovernmentExtendedIndicators
        extend_indicators = GovernmentExtendedIndicators.objects.create(
            government=instance,
            bonds_nominal_profit=round(indicators_tupple[0], 2),
            coupons_cost_difference=round(indicators_tupple[1], 2),
            coupons_profit=round(indicators_tupple[2], 2),
            current_rate=round(indicators_tupple[3], 2))
            # Зберігаємо новий запис
        extend_indicators.save()


# # ФУНКЦІЯ АВТОМАТИЧНОГО РОЗРАХУНКУ ТА ЗАПИСУ ПЕРІОДУ ДІЇ ОВДП (ЗГІДНО ВЕДЕНИХ ДАТ)
# def definition_period(instance, **kwargs):
#     # Перевіряємо чи поле period null (щоб не було неконтрольованої рекурсії - зациклення)
#     # Зациклення виникає коли викликається метод save() - зберегти обєкт в БД, тоді знову спрацьовує @receiver,
#     # знову запускає ф-ю з розрахунком періоду і знову метод save() і так по колу ...
#     if instance.period is None:
#         # викликаємо ф-ю defining_period розрахунку періоду з utils.governments.gov_func
#         instance.period = defining_period(instance)
#         instance.save()


# Розрахунок та заповнення таблиці : GovernmentIndicators
# def calculate_and_save_product_indicators(sender, instance, created, **kwargs):
#
#     # перевіряємо чи рік високосний (високосний-366днів)
#     is_leap_year = calendar.isleap(instance.end_date.year)
#     # контрольна дата 28 Лютого (високосний рік 29 Лютого)
#     control_date = date(instance.end_date.year, 2, 28)
#
#     # Якщо термін звершення депозиту у високосний рік більший за 28 Лютого тоді 366 днів інакше 365
#     if is_leap_year and instance.end_date > control_date:
#         # Обчислюємо показники(доходи - день , міс,рік,загальний) для вхідного продукту
#         product_values = calculate_product_indicators(instance, 366)
#     else:
#         # Обчислюємо показники(доходи - день , міс,рік,загальний) для вхідного продукту
#         product_values = calculate_product_indicators(instance, 365)
#
#     # Перевіряємо, чи створено новий продукт
#     # При створенні нового продукту created = true, тоді створюється запис у БД
#     # Нижче перевіряємо який продукт ми отримали на вході , якщо Deposit у відповідній таблиці і створюється запис
#     if created :
#         # Створюємо новий запис у таблиці Deposits
#         indicators = GovernmentIndicators.objects.create(
#             government=instance,
#             dayily_profit=round(product_values[0], 2),
#             month_profit=round(product_values[1], 2),
#             year_profit=round(product_values[2], 2),
#             total_profit=round(product_values[3], 2)
#         )
#         # Зберігаємо новий запис
#         indicators.save()

