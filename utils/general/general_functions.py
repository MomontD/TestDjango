
# МОДЕЛЬ ІНДИКАТОРІВ ПРОДУКТІВ (ДЕННИЙ,МІСЯЧНИЙ,РІЧНИЙ,ЗАГАЛЬНИЙ ДОХОДИ)
class ListOfValues:
    def __init__(self, currency, calc_sum, average_rate, dayily_profit, monthly_profit, year_profit, total_profit, current_rate):
        self.currency = currency
        self.calc_sum = calc_sum
        self.average_rate = average_rate
        self.dayily_profit = dayily_profit
        self.monthly_profit = monthly_profit
        self.year_profit = year_profit
        self.total_profit = total_profit
        self.current_rate = current_rate  # Для ОВДП / середній фактичний %


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


# ФУНКЦІЯ СУМУВАННЯ ІНДИКАТОРІВ ЗГРУПОВАНИХ ПРОДУКТІВ ПО ВАЛЮТАМ (ДЕННИЙ,МІСЯЧНИЙ,РІЧНИЙ,ЗАГАЛЬНИЙ ДОХОДИ)
def calculate_indicators(name_instance,grouped_data):
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
        # Фактичний відсоток по ОВДП
        current_rate = 0
        # Загальний дохід з депозитам , позикам
        total_profit = 0

        # Умова, якщо група не порожня - провести калькуляцію показників групи
        # Чому група може бути порожньою ? Тому , що створюється масив [[UAH],[USD] .. [PLN]], з якого [PLN] може бути порожнім і всі інші
        if group:
            for element in group:
                calc_sum += round(element.sum, 2)
                currency = element.currency
                average_rate += element.rate

                if name_instance == 'loans':
                    product_indicators = element.loans_indicators.get()  # витягуємо дані з звязвної таблиці loans_indicators
                if name_instance == 'deposits':
                    product_indicators = element.deposits_indicators.get()
                if name_instance == 'governments':
                    product_indicators = element.governments_indicators.get()
                    # Розраховуємо середній фактичний % для ОВДП
                    extended_indicators = element.governments_extended_indicators.get()
                    current_rate_from_table = extended_indicators.current_rate
                    current_rate += current_rate_from_table

                dayily_profit += product_indicators.dayily_profit
                monthly_profit += product_indicators.month_profit
                year_profit += product_indicators.year_profit
                total_profit += product_indicators.total_profit
                counter += 1

            average_rate = round(average_rate/counter, 2)      # Визначення середнього % по депозитам
            current_rate = round(current_rate/counter, 2)
            res_calc = ListOfValues(
                currency, round(calc_sum, 2), round(average_rate, 2), round(dayily_profit, 2),
                round(monthly_profit, 2), round(year_profit, 2), round(total_profit, 2), round(current_rate, 2)
                                    )
            values_for_report.append(res_calc)

    return values_for_report

def calculate_product_indicators(instance, days):

    # Якщо поле таблиці auto_capitalization == 'not apply' тобто '0' - стандартний розрахунок
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
