'''
Задание:
Для функції get_pb_exchange_rate створити валідатор на отримане значення дати. Користувач може вводити дату через дефіс
або злитно (01112022) і функція має працювати коректно. За іншого варіанту видавати повідомлення, що дату ввели не коректно.
'''
def convert_time(date: str) -> str:
    '''
    функция проверяет корректность введенной даты, в случае неподдерживаемых API банка разделителей, преобразует в
    корректный формат и возвращает отформатированный вариант.
    Варианты ввода: д-м-гг, д.м.гг, д/м/гг и без разделителей дмгг или д м гг
    Любые другие  введенные данные будут считаться неопределенными и вернется сообщение об ошибке
    :param date: введенная дата
    :return: отформатированная дата
    '''
    # P.S. Реализовал чуть больше проверок, для практики

    var_separator = ['.', '-', '/', ',']
    err = 'no date format defined'
    date = date.replace(' ', '')
    if len(date) == 10:
        separator = date[2]


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


# d = convert_time('01118888')

# d = convert_time('01 11 9999')

# d = convert_time ('01-11-2022')

# d = convert_time ('01.11.2018')

# d = convert_time ('01/11/2018')

d = convert_time ('01,11,2018')

# d = convert_time('011188886')

# d = convert_time('dddddddd')

# d = convert_time('dd dd dddd')

# d = convert_time('01.Y1.2022')

# d = convert_time('01 1     188    88')

print(d)
