
#  Таблиця для валюти по міжбанку ( нижче ще додаткова ф-я , таблиці по даним чорного ринку , підхід аналогічний
def data_for_currency_table_bank (table) : # отримую на вхід таблицю в HTML форматі

    # headers = ['Валюта','Купівля','Динаміка','Продаж','Динаміка','Курс НБУ','Динаміка']
    headers = []                           # буде масив з заголовками
    for th in table.find_all('th'):        # в циклі забираю заголовки і додаю їх в масив
        headers.append(th.text.strip())

    incomming_currens_data = []            # наповнення таблиці (дані , курси валют)
    for tr in table.find_all('tr'):        # шукаю рядки а в рядках стовпці і забираю курси
        row = []                           # в результаті я отримую масив з масивів :
        for td in tr.find_all('td'):       # incomming_currens_data = [[USD,38,40,-0.03],[EUR,40,42б,0.05],[PLN,8,9,0.00]]
            row.append(td.text.strip())
        if row:
            incomming_currens_data.append(row)

    currens_data = []

    for mass in incomming_currens_data: # тут я відфільтровую(забираю) показники динаміки які потрапили мені в масив до кожної валюти :
                                        # -0.03 , 0.05 , 0.00
        temp = []

        for el in mass :
            if len(el) > 3:
                temp.append(el[:6])
                # temp.append(el[7:len(el)])
            else:
                temp.append(el)

        currens_data.append(temp)

    return {'headers': headers , 'currens_data': currens_data }

#  Таблиця для валюти "чорний ринок" , підхід аналогічний як для міжбанку - дивись опис таблиці вище
def data_for_currency_table_cash (table) :

    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())

    incomming_currens_data = []
    for tr in table.find_all('tr'):
        row = []
        for td in tr.find_all('td'):
            row.append(td.text.strip())
        if row:
            incomming_currens_data.append(row)

    currens_data = []

    for mass in incomming_currens_data:
        temp = []

        for el in mass :
            if len(el) > 3:
                temp.append(el[:5])
            else:
                temp.append(el)

        currens_data.append(temp)

    return {'headers': headers , 'currens_data': currens_data }

# currens_data = [el for el in all_currens_data if el[1] in ['UAH', 'USD', 'EUR', 'PLN', 'CHF', 'GBP']] для сайту НБУ
# headers[4] = headers[4][:14] для сайту НБУ