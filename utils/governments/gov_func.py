
# ФУНКЦІЯ З АВТОМАТИЧНОГО РОЗРАХУНКУ ПЕРІОДУ ДЛЯ ОВДП
def defining_period(instance):

    # Вираховуємо різницю в днях (початкова дата - дата розірвання)
    # Таке рівняння можливе за допомогою модуля datetime
    difference = instance.end_date - instance.start_date
    # За допомогою методу .days отримуємо дні
    number_of_month = round(difference.days/30)
    # Повертаємо заокруглені місяці (...< 1.5 = 1 , 1.5 < ... = 2)
    return number_of_month


def calculate_base_bonds_indicators(instance):
    # Чистий дохід по ОВДП - сума виплати - суму вкладу - витрати
    clean_bonds_profit = instance.bonds_repayment_nominal - instance.sum - instance.bonds_expenses
    difference = instance.end_date - instance.start_date
    dayily_profit = clean_bonds_profit / difference.days
    month_profit = clean_bonds_profit / instance.period
    # total_profit = (instance.sum * (instance.rate / 100)) * (instance.period / 12)

    # Якщо депозит менший за 12 міс. його загальний дохід рахується як річний
    if instance.period <= 12:
        year_profit = clean_bonds_profit
    # Якщо депозит більший за 12 міс. , рахуємо дохід тільки за 12 міс.
    else:
        year_profit = (clean_bonds_profit/instance.period) * 12

    return [dayily_profit, month_profit, year_profit, clean_bonds_profit]


# ФУНКЦІЯ ДЛЯ РОЗРАХУНКУ РОЗШИРЕНИХ ПОКАЗНИКІВ ОВДП (ДЛЯ ТАБЛИЦІ GovernmentExtendedIndicators)
def calc_extends_indicators (instance):

    # Номінальний дохід
    nominal_profit = instance.bonds_repayment_nominal - (instance.coupons_nominal_cost * instance.coupons)
    # Різниця вартості купонів між номінальною і фактичною
    coupons_difference = instance.coupons_nominal_cost - instance.coupons_current_cost
    # Купонний дохід/збиток
    all_coupons_profit = coupons_difference * instance.coupons
    #  Фактичний дохід (Загальна сума виплат по облігаціям - фактичну суму вкладу ОВДП)
    bonds_income = instance.bonds_repayment_nominal - instance.sum - instance.bonds_expenses
    # Фактичний %
    bonds_year_profit = (bonds_income / instance.period) * 12  # Річний дохід
    # визначення річного % - (річний дохід / суму вкладу)* 100
    bonds_rate = (bonds_year_profit / instance.sum) * 100

    return nominal_profit, bonds_income, coupons_difference, all_coupons_profit, bonds_rate


# Ф-я яка формує обєкт з роками та місяцями коли присутні платежі по ОВДП
def forming_period_list (date_list):
    # date_list - отримуємо на вході актуальний + відсортований список(з меншої дати до більшої) з платежами по ОВДП
    period_list = {}
    # Проганяємо через цикл кожен елемент списку
    for date in date_list:
        # Вибираємо з елементу дату(рік) якщо такого нема в словнику додаємо
        if date.payment_date.year not in period_list:
            period_list[date.payment_date.year] = []
        # Вибираємо місяць з елементу, якщо такого немає в словнику з роком({'2023': ['Jan',...] додаємо до року
        if date.payment_date.strftime('%B') not in period_list[date.payment_date.year]:
            period_list[date.payment_date.year].append(date.payment_date.strftime('%B'))

    # Повертає :
    # перший : {2023: ['June', 'August', 'November'], 2024: ['February', 'May', 'August'], 2025: ['February']}
    return period_list


# Ф-я яка формує обєкт з підсумковими платежами по кожному року (купони та повернення ОВДП)
def forming_year_payments_list (period_list, payments_list):

    year_payments_list = {}

    for payment in payments_list:
        for year in period_list:
            if payment.payment_date.year == year:
                if payment.payment_date.year not in year_payments_list:
                    year_payments_list[payment.payment_date.year] = {}

                if payment.payment_type not in year_payments_list[payment.payment_date.year]:
                    year_payments_list[payment.payment_date.year][payment.payment_type]= 0

                year_payments_list[payment.payment_date.year][payment.payment_type] += payment.payment_sum
    # Повертає :
    # {2023: {'coupons': 100864.85, 'government sum': 911000.0}, 2024: {'coupons': 91517.0, 'governm
    # ent sum': 180000.0}, 2025: {'coupons': 41263.0, 'government sum': 521000.0}}
    return year_payments_list

