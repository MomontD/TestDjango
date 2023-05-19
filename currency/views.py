from currency.static.currency.py.def_for_currency import *
from django.shortcuts import render
import datetime

import requests
from bs4 import BeautifulSoup

def currency (request) :                                    # Будемо зчитувати дані з сайту мінфін https://minfin.com.ua/ua/currency/

    url_minfin = 'https://minfin.com.ua/ua/currency'        # вказуємо лінк де знаходяться курси валют
    response_minfin = requests.get(url_minfin)              # записуємо в змінну результат звернення на сторінку
                                                            # якщо все ок будуть знаходитись дані сторінки
    if response_minfin.status_code == 200:                  # Перевіряємо чи запит успішний (код 200)

        soup = BeautifulSoup(response_minfin.text, 'html.parser')    # В змінну soup записуємо дані сторінки в HTML форматі / парсимо в HTML

        # Курси по міжбанку і чорному ринку знаходяться в одній таблиці але розитій по різним <div>
        # Відповідно потрібно знайти перший <div> в ньому таблицю і витягнути дані і по аналогу з другим <div>
        # Пошук по першому <div> не роблю , достатньо зробити пошук по class таблиці і "перше" входження буде в першому <div>
        # Другу частину таблиці вже шукаю через другий <div>

        # Дані для таблиці курсц валют міжбанк і НБУ
        # Знаходжу актуальну дату на яку софрмовані курси валют , ділю її .split(',')[0] і беру 1 елемент(дату) бо вона відображає ще час
        actual_date = soup.find('div', {'class': 'sc-1pskrw4-0 etyNYJ'}).text.strip().split(',')[0]
        # actual_time = datetime.datetime.now()
        table_for_bank = soup.find('table', {'class' : 'sc-1x32wa2-1 dYkgjk'})  # шукаю таблицю за class
        # підключаю ф-ю з static/py/def_for_currency для формування даних для відображення
        # Таблиця містить ще динаміку курсу (показники - цифри) їх я забираю і залишаю сам курс
        data_for_table_bank = data_for_currency_table_bank(table_for_bank)

        # Дані для таблиці курсц валют готівка (чорний ринок)
        div = soup.find('div', {'class': 'sc-1x32wa2-0 dWgyGF bvp3d3-10 bvp3d3-11 kNRLfR cLIHts'})
        table_for_cash = div.find('table', {'class': 'sc-1x32wa2-1 dYkgjk'})
        data_for_table_cash = data_for_currency_table_cash(table_for_cash)
        print(data_for_table_cash)


    else:
        return response_minfin.status_code

    print(actual_date)
    return render (request, 'currency/currency.html', {'data_for_table_bank' : data_for_table_bank,
                                                       'data_for_table_cash': data_for_table_cash,
                                                       'actual_date' : actual_date,
                                                       #'actual_time' : actual_time
                                                                                    })


    # Робочий варіант з НБУ#######################################################
    # url_nbu = 'https://bank.gov.ua/ua/markets/exchangerates'
    # response_nbu = requests.get(url_nbu)
    #
    # if response_nbu.status_code == 200:
    #     soup = BeautifulSoup(response_nbu.text, 'html.parser')
    #
    #     date = soup.find('span', {'id': 'exchangeDate'}).text.strip()
    #     table = soup.find('table', {'id': 'exchangeRates'})
    #
    #     data_for_table = data_for_currency_table (table)   #функція з currency.static.currency.py
    #
    # else:
    #     return response_nbu.status_code

    # return render (request, 'currency/currency.html', {'date': date,
    #                                                    'data_for_table': data_for_table })
    #####################################################################################



# def get_exchange_rates():
#     url = "https://bank.gov.ua/ua/markets/exchangerates"
#     params = {'valcode': ['USD', 'EUR']}
#     response = requests.get(url, params=params)
#
#     # Перевірка на код статусу 200 OK
#     if response.status_code == 200:
#         # Повертаємо дані у вигляді словника або списку
#         return response.content
#     else:
#         # Якщо статус не 200, повертаємо порожній словник або список
#         return 'ERROR'


# def get_date_currency (request) :
#     url = 'https://bank.gov.ua/ua/markets/exchangerates'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     date = soup.find('div', {'class': 'date'}).text.strip()
