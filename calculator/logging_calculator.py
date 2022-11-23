from datetime import datetime as dt


def calcus_logger(resault, expression):  # Логирование для калькулятора, Принимает результат работы калькулятора
    time = dt.now().strftime("%d.%m.%Yг. %H:%M")  # Создаем time в формате день, месяц, год + часы +минуты события
    with open('log_calcus.csv', 'a') as file:  # добавляем файл "log_calcus.csv" - Журнал калькулятора
        file.write('{}; Пример: {} Ответ:  {}\n'.format(time, expression,
                                                        resault))  # записываем в наш файл дату события и резул.калькулятора
    with open('log.csv', 'a') as file:  # добавляем файл "log.cvs" на запись - Журнал всех событий
        file.write('{}; Пример: {} Ответ:  {}\n'.format(time, expression,
                                                        resault))  # записываем в него дату события и результат калькулятора


#  Логирование Входа,Выхода пользователя из программы и обработки ошибок!
def common_logger(data):
    time = dt.now().strftime("%d.%m.%Yг. %H:%M")  # создаем time в формате день, месяц, год + часы +минуты события
    with open('log.csv', 'a') as file:  # добавляем файл "log.cvs" Журнал всех событий
        file.write('{};  {}\n'.format(time, data))  # записываем дату события и вход/выход в программу или ошибки


