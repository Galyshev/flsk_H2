import time

import requests

from datetime import datetime
from urllib import parse


def get_currency_iso_code(currency: str) -> int:
    '''
    Функція повертає ISO код валюти
    :param currency: назва валюти
    :return: код валюти
    '''
    currency_dict = {
        'UAH': 980,
        'USD': 840,
        'EUR': 978,
        'GBP': 826,
        'AZN': 944,
        'CAD': 124,
        'PLN': 985,
    }
    try:
        return currency_dict[currency]
    except:
        raise KeyError('Currency not found! Update currencies information')


def get_currency_exchange_rate(currency_a: str,
                               currency_b: str) -> str:
    currency_code_a = get_currency_iso_code(currency_a)
    currency_code_b = get_currency_iso_code(currency_b)

    response = requests.get('https://api.monobank.ua/bank/currency')
    json = response.json()

    if response.status_code == 200:
        for i in range(len(json)):
            if json[i].get('currencyCodeA') == currency_code_a and json[i].get('currencyCodeB') == currency_code_b:
                date = datetime.fromtimestamp(
                    int(json[i].get('date'))
                ).strftime('%Y-%m-%d %H:%M:%S')
                rate_buy = json[i].get('rateBuy')
                rate_sell = json[i].get('rateSell')
                return f'exchange rate {currency_a} to {currency_b} for {date}: \n rate buy - {rate_buy} \n rate sell - {rate_sell}'
            return f'Not found: exchange rate {currency_a} to {currency_b}'
    else:
        return f"Api error {response.status_code}: {json.get('errorDescription')}"




#print(get_currency_exchange_rate('USD', 'UAH'))


def convert_time(date: str) -> str:
    '''
    функция проверяет корректность введенной даты, в случае неподдерживаемых API банка разделителей, преобразует в
    корректный формат и возвращает отформатированный вариант.
    Варианты ввода: д-м-гг, д.м.гг, д/м/гг и без разделителей дмгг или д м гг
    Любые другие  введенные данные будут считаться неопределенными и вернется сообщение об ошибке
    :param date: введенная дата
    :return: отформатированная дата
    '''

    var_separator = ['.', '-', '/', ' ']
    err = 'no date format defined'

    if len(date) == 10:
        separator = date[2]
    # дата введена верно (через точку)
        if separator == '.':
            return date

    # дата введена через поддерживаемый для обработки разделитель
        for sep in var_separator:
            if sep == separator:
                tmp = date.split(separator)
                if tmp[0].isdecimal() and tmp[1].isdecimal() and tmp[2].isdecimal():
                    day = tmp[0]
                    month = tmp[1]
                    year = tmp[2]
                    return day + '.' + month + '.' + year

        return err

    # дата введена верно, но без разделителей
    if len(date) == 8:
        day = date[:2]
        month = date[2:4]
        year = date[-4:]
        if day.isdecimal() and month.isdecimal() and year.isdecimal():
            return day + '.' + month + '.' + year
        else:
            return err
    # дата введена не корректно (по любой причине)
    else:
        return err


def get_pb_exchange_rate(convert_currency: str,
                         bank: str,
                         rate_date: str) -> str:
    chk_rate_date = convert_time(rate_date)
    if chk_rate_date == 'no date format defined':
        return f'error: {chk_rate_date}'
    params = {
        'json': '',
        'date': chk_rate_date,
    }
    query = parse.urlencode(params)
    api_url = 'https://api.privatbank.ua/p24api/exchange_rates?'
    response = requests.get(api_url+query)
    json = response.json()
    if response.status_code == 200:
        rates = json['exchangeRate']
        for rate in rates:
            if rate['currency'] == convert_currency:
                if bank == 'NBU':
                    try:
                        sale_rate = rate['saleRateNB']
                        purchase_rate = rate['purchaseRateNB']
                        return f'Exchange rate UAH to {convert_currency} for {chk_rate_date} at {bank}: sale={sale_rate}, purchase={purchase_rate}'
                    except:
                        return f'There is no exchange rate NBU for {convert_currency}'
                elif bank == 'PB':
                    try:
                        sale_rate = rate['saleRate']
                        purchase_rate = rate['purchaseRate']
                        return f'Exchange rate UAH to {convert_currency} for {chk_rate_date} at {bank}: sale={sale_rate}, purchase={purchase_rate}'
                    except:
                        return f'There is no exchange rate PrivatBank for {convert_currency}'
    else:
        return f'error {response.status_code}'


result = get_pb_exchange_rate('USD', 'PB', '01/11/2022')
print(result)
time.sleep(10)
# result = get_pb_exchange_rate('USD', 'PB', '02-11-2022')
# print(result)
# time.sleep(10)
# result = get_pb_exchange_rate('USD', 'PB', '03112022')
# print(result)
# time.sleep(10)
result = get_pb_exchange_rate('USD', 'PB', '0311')
print(result)


