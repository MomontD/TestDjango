
def defining_period(instance):

    # Вираховуємо різницю в днях (початкова дата - дата розірвання)
    # Таке рівняння можливе за допомогою модуля datetime
    difference = instance.end_date - instance.start_date
    # За допомогою методу .days отримуємо дні
    number_of_month = round(difference.days/30)
    # Повертаємо заокруглені місяці (...< 1.5 = 1 , 1.5 < ... = 2)
    return number_of_month


