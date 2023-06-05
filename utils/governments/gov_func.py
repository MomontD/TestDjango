
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


def forming_list_of_years (date_list):

    list_of_years = []
    # Витягйємо рік з дати оплати і додаємо його в масив / результат = масив з роками
    for el in date_list:
        list_of_years.append(el.payment_date.year)
    # Забираємо дублікати з масиву років та відсортовуємо унікальнізначення = [2022,2023,2024]
    list_of_years = sorted(set(list_of_years))

    return list_of_years