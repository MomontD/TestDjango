
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
    nominal_profit = instance.bonds_repayment_nominal - instance.sum
    # Різниця вартості купонів між номінальною і фактичною
    coupons_difference = instance.coupons_nominal_cost - instance.coupons_current_cost
    # Купонний дохід/збиток
    all_coupons_profit = coupons_difference * instance.coupons
    # Фактичний %  = (Загальна сума виплат - суму вкладу ОВДП + дохід/збиток від вартості купону)
    bonds_profit = nominal_profit + all_coupons_profit  # Загальний дохід
    bonds_year_profit = (bonds_profit / instance.period) * 12  # Річний дохід
    # % - (річний дохід / суму вкладу)* 100
    bonds_rate = ((bonds_year_profit - instance.bonds_expenses) / instance.sum) * 100
    print(nominal_profit, coupons_difference, all_coupons_profit, bonds_rate)

    return nominal_profit, coupons_difference, all_coupons_profit, bonds_rate
