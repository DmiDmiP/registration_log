# -*- coding: utf-8 -*-

from os import path, remove


class NoteEmailError(Exception):
    pass


class NotNameError(Exception):
    pass


def writeinfile(name, str):
    with open(name, mode='a') as log:
        log.write(str + '\n')


if path.exists('registrations_good.log'):
    remove('registrations_good.log')
if path.exists('registrations_bad.log'):
    remove('registrations_bad.log')

with open('registrations.txt', mode='r') as file:
    for line in file:
        line = line[:-1]
        try:
            name, email, age = line.split(' ')
            if name.isalpha():
                if '@' and '.' in email:
                    if age.isnumeric():
                        age = int(age)
                        if 9 < age < 100:
                            writeinfile(name='registrations_good.log', str=f'{name} {email} {age}')
                        else:
                            raise ValueError('Слишком стар')
                    else:
                        raise ValueError('поле возраст НЕ является числом')
                else:
                    raise NoteEmailError('Нет @ или . в адресе почты')
            else:
                raise NotNameError('поле имени содержит НЕ только буквы')


        except ValueError as exp:
            if 'unpack' in exp.args[0]:
                writeinfile(name='registrations_bad.log', str=f'Не хватает введенных данных {exp} в строк {line}')
            elif 'от 10 до 99' in exp.args[0]:
                writeinfile(name='registrations_bad.log', str=f'{exp} в строке {line}')
        except NoteEmailError as exp:
            writeinfile(name='registrations_bad.log', str=f'{exp} в строке {line}')
        except NotNameError as exp:
            writeinfile(name='registrations_bad.log', str=f'{exp} в строке {line}')
