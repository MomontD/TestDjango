
# ФУНКЦІЯ З АВТОМАТИЧНОГО РОЗРАХУНКУ ПЕРІОДУ ДЛЯ ОВДП
def defining_period(instance):

    # Вираховуємо різницю в днях (початкова дата - дата розірвання)
    # Таке рівняння можливе за допомогою модуля datetime
    difference = instance.end_date - instance.start_date
    # За допомогою методу .days отримуємо дні
    number_of_month = round(difference.days/30)
    # Повертаємо заокруглені місяці (...< 1.5 = 1 , 1.5 < ... = 2)
    return number_of_month


# ФУНКЦІЯ ДЛЯ РОЗРАХУНКУ РОЗШИРЕНИХ ПОКАЗНИКІВ ОВДП (ДЛЯ ТАБЛИЦІ GovernmentExtendedIndicators)
def calc_extends_indicators (instance):

    # Номінальний дохід
    nominal_profit = instance.bonds_repayment_nominal - (instance.coupons_nominal_cost * instance.coupons)
    # Різниця вартості купонів між номінальною і фактичною
    coupons_difference = instance.coupons_nominal_cost - instance.coupons_current_cost
    # Купонний дохід/збиток
    all_coupons_profit = coupons_difference * instance.coupons
    #  Фактичний дохід (Загальна сума виплат по облігаціям - фактичну суму вкладу ОВДП)
    bonds_income = instance.bonds_repayment_nominal - instance.sum
    #  Фактичний ПРИБУТОК !!! (Загальна сума виплат - суму вкладу ОВДП - видатки + дохід/збиток від вартості купону)
    actual_profit = (bonds_income - instance.bonds_expenses) + all_coupons_profit
    # Різниця доходів ( номінальний/фактичний)
    difference_income = bonds_income - nominal_profit
    # Фактичний %
    bonds_year_profit = (actual_profit / instance.period) * 12  # Річний дохід
    # визначення річного % - (річний дохід / суму вкладу)* 100
    bonds_rate = ((bonds_year_profit - instance.bonds_expenses) / instance.sum) * 100
    print(nominal_profit, actual_profit, coupons_difference, all_coupons_profit, bonds_rate)

    return nominal_profit, bonds_income, difference_income, actual_profit, \
        coupons_difference, all_coupons_profit, bonds_rate
