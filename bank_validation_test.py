'''
Задание
Для функції get_pb_exchange_rate створити валідатор на отримане значення банку. Користувач може вводити наступні
значення: NBU, nbu, PB, pb, PrivatBank, Privatbank і функція має з ними працювати коректно. За інших значень вивести
повідомлення про некоректний банк
'''

def chk_bank(bank: str) -> str:
    '''
    Функция принимает на вход абревиатуру банка, проверяет с заданными и возвращает либо буквенный код банка
    либо ошибку, если были ввведены не корректные символы

    :param bank: буквенное обозначение банка от пользователя
    :return: код банка либо ошибка, если банк не найден
    '''
    # перевод значений в нижний регистр, чтобы любое сочетание правильных абревиатур указывало на корректный банк
    bank = bank.lower().replace(' ', '')
    if bank == 'nbu':
        return 'NBU'
    elif bank == 'pb' or bank == 'privatbank':
        return 'PB'
    else:
        return 'error'

# b = chk_bank('NBU')
# b = chk_bank('nbu')
# b = chk_bank('PB')
# b = chk_bank('pb')
# b = chk_bank('PrivatBank')
# b = chk_bank('Privatbank')
# b = chk_bank('Pri vat ban  k')
# b = chk_bank('PriVatbAnk')
b = chk_bank('fgghfgdgdh')

print(b)
