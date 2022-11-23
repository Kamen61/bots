import re
import logging_calculator as lg

symbols = r'[^\.\+\-\*\/\(\)0-9ij]'
actions = ['+', '-', '*', '/', '^']


def str_check(task):
    if re.search(symbols, task):  # если есть не числа, не арифметические символы, не i и не j
        data = 'Обнаружена ошибка ввода данных! Ошибка:' + task
        lg.common_logger(data)
        return False
    else:
        if 'i' in task and 'j' in task:  # если сразу и i, и j
            data = 'Обнаружена ошибка ввода данных! Ошибка: ' + task
            lg.common_logger(data)
            return False
        if not (re.search('[\d]', task) and re.search('[\+\-\*\/]', task)):  # если только цифры или только ариф.символы
            data = 'Обнаружена ошибка ввода данных! Ошибка: ' + task
            lg.common_logger(data)
            return False
        for i in range(len(task)):  # если вокруг ариф.символов нет чисел
            if task[i] in actions:
                if not(task[i-1].isdigit and task[i+1].isdigit):
                    data = 'Обнаружена ошибка ввода данных! Ошибка:' + task
                    logging.common_logger(data)
                    return False
        return True
