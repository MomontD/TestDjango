

################## ОПЕРАЦІЇ З ДЕПОЗИТАМИ ##############################################################################

# ФОРМА ДЛЯ МАСИВУ З ПОКАЗНИКІВ ДЕПОЗИТУ (ДЕНЮ,МІС,рІС ДОХОДИ)
class ListOfValues:
    def __init__(self, currency, calc_sum, average_rate, dayily_profit, monthly_profit, year_profit, total_profit):
        self.currency = currency
        self.calc_sum = calc_sum
        self.average_rate = average_rate
        self.dayily_profit = dayily_profit
        self.monthly_profit = monthly_profit
        self.year_profit = year_profit
        self.total_profit = total_profit


# ФУНКЦІЯ ГРУПУВАННЯ ДЕПОЗИТІВ ПО ВАЛЮТАМ
def grouping(incoming_data):
    # Отримуємо на вхід депозити з БД (активні або архівні, в залежності що передамо)
    # Створюємо під кожний депозит масив валюти до якої він належить і в циклі групуємо
    # Далі через return передаємо масив масивів депозитів
    group_uah = []
    group_usd = []
    group_eur = []
    group_pln = []
    group_chf = []
    group_gbp = []

    for element in incoming_data:
        if element.currency == 'UAH':
            group_uah.append(element)
        if element.currency == 'USD':
            group_usd.append(element)
        if element.currency == 'EUR':
            group_eur.append(element)
        if element.currency == 'PLN':
            group_pln.append(element)
        if element.currency == 'CHF':
            group_chf.append(element)
        if element.currency == 'GBP':
            group_gbp.append(element)

    if group_uah or group_usd or group_eur or group_pln or group_chf or group_gbp:
        return [group_uah, group_usd, group_eur, group_pln, group_chf, group_gbp]

    else:
        return 'list is empty'


# РОЗРАХУНОК ПОКАЗНИКІВ ПІД ЧАС СТВОРЕННЯ ДЕПОЗИТУ/ПОЗИКИ
def calculate_values(instance, days):

    # Якщо поле таблиці auto_capitalization == 'not apply' тобто '0' - стандартний розрахунок
    if instance.auto_capitalization == 0:
        dayily_profit = instance.sum * (instance.rate / 100) / days
        month_profit = (instance.sum * (instance.rate / 100)) * (instance.period / 12) / instance.period
        total_profit = (instance.sum * (instance.rate / 100)) * (instance.period / 12)

        # Якщо депозит менший за 12 міс. його загальний дохід рахується як річний
        if instance.period <= 12:
            year_profit = total_profit
        # Якщо депозит більший за 12 міс. , рахуємо дохід тільки за 12 міс.
        else:
            year_profit = instance.sum * (instance.rate / 100)

        return [dayily_profit, month_profit, year_profit, total_profit]

    # Якщо поле таблиці auto_capitalization застосоване - розрахунок доходу депозиту згідно обраної частоти капіталізації
    else:
        total_profit = (instance.sum * (1 + (instance.rate / 100) / instance.auto_capitalization) **
                        (instance.auto_capitalization * (instance.period/12))) - instance.sum
        month_profit = total_profit / instance.period
        dayily_profit = total_profit / (days * instance.period / 12)

        # Якщо депозит менший або дорвнює 12 міс. його загальний дохід рахується як річний
        if instance.period <= 12:
            year_profit = total_profit
        # Якщо депозит більший за 12 міс. , рахуємо дохід тільки за 12 міс.
        else:
            year_profit = (instance.sum * (1 + (instance.rate / 100) / instance.auto_capitalization) **
                        instance.auto_capitalization) - instance.sum

        return [dayily_profit, month_profit, year_profit, total_profit]


# КАЛЬКУЛЯЦІЯ ПОКАЗНИКІВ ДЛЯ ЗВІТУ report в HTML
def calculate_data(grouped_data):
    # Отримуємо на вхід (grouped_data) масив з групованих депозитів (по валюті)

    values_for_report = []

    # Проганяємо з масиву кожну групу валютного депозиту
    for group in grouped_data:
        # лічильник ітерацій циклу / необхідний для обрахування середнього %
        counter = 0
        # Обрахунок загальної суми депозитів / позик
        calc_sum = 0
        currency = ''
        dayily_profit = 0
        monthly_profit = 0
        year_profit = 0
        # Середній відсоток по депозитам , позикам
        average_rate = 0
        # Загальний дохід з депозитам , позикам
        total_profit = 0

        # Умова, якщо група не порожня - провести калькуляцію показників групи
        # Чому група може бути порожньою ? Тому , що створюється масив [[UAH],[USD] .. [PLN]], з якого [PLN] може бути порожнім і всі інші
        if group:
            for element in group:
                calc_sum += element.sum
                currency = element.currency
                average_rate += element.rate

                deposit_indicators = element.deposits_indicators.get()  # витягуємо дані з звязвної таблиці deposit_indicators

                dayily_profit += deposit_indicators.dayily_profit
                monthly_profit += deposit_indicators.month_profit
                year_profit += deposit_indicators.year_profit
                total_profit += deposit_indicators.total_profit
                counter += 1

            average_rate = round(average_rate/counter, 2)      # Визначення середнього % по депозитам
            res_calc = ListOfValues(currency, round(calc_sum,2), round(average_rate,2), round(dayily_profit, 2),
                                    round(monthly_profit,2), round(year_profit,2), round(total_profit,2))
            values_for_report.append(res_calc)

    return values_for_report

# Формула розрахунку складних %
# Для розрахунку складних відсотків існує спеціальна формула:
# FV = PV × (1 + r/n)^(n×t)
# де:
# FV - майбутня (майже завжди більша) вартість вкладу, який враховує складні відсотки.
# PV - початкова вартість вкладу.
# r - річна процентна ставка.
# n - число разів, коли відсотки нараховуються за рік.
# t - кількість років, на які вклад буде розміщено.
# Отже, для розрахунку складних відсотків потрібно враховувати частоту нарахування відсотків за рік (n). Якщо відсотки нараховуються щорічно, то n = 1, якщо півріччями, то n = 2, кварталами - n = 4, місячні відсотки - n = 12 і т.д.
# Наприклад, якщо ви розмістите вклад на 1000 доларів під 5% річних зі складними відсотками, які нараховуються щомісяця, на 2 роки, то майбутня вартість вкладу буде:
# FV = 1000 × (1 + 0.05/12)^(12×2) = 1104.08 доларів.
# Отже, після 2 років вартість вашого вкладу збільшиться до 1104.08 доларів з початкових 1000 доларів, якщо ви зможете зберігати гроші на вкладі протягом усього терміну депозиту і банк не змінить умови вкладу.

# Формула розрахунку стандартних %
# Визначення місячного доходу по депозитам :
#  - Записуємо в масив місячний дохід по кожному депозиту і потім сумуємо значення
#  - Формула : місячний дохід = сума депозиту * ставка % * період (12міс.-1, 6міс.-0,5, 3 міс. - 0,25) - тут ми
#    дізнаємось загальний дохід від депозиту , далі ділимо на період 12,6,3міс.
#  - Приклад : 100 000 грн * 18% * 1 = 18 0000 грн / 12міс. = 1 500 грн в міс.
# Визначення загального доходу по депозитам :
# Формула : Основна сума * Ставка * Період часу/12
# Капіталізація % :
# Депозит 1 000 грн , 22% річних , 12 міс.
# 1. Беремо депозит і проганяємо в циклі відповідно до терміну (к-сть місяців)
# 2. Вираховуємо % за кожен місяць і додаємо їх до тіла депозиту кожен раз при ітерації циклу
# 3. Загальний дохід = Проітерований депозит з % - початкову суму депозиту.
