import telebot


def creat_array():
    array = []
    for i in range(3):
        array_1 = []
        for j in range(3):
            array_1.append('+')
        array.append(array_1)
    return array


def print_array(array):
    result = ''
    for i in range(3):
        result += ("  ".join(array[i]))
        result += '\n'
    return result


def chek_win(array):
    win = '-'
    result_diagonal_left = ''
    result_diagonal_right = ''
    for i in range(3):
        result_line = ''
        result_row = ''
        for j in range(3):
            result_line += array[i][j]          #Проверка строки
            result_row += array[j][i]               #Проверка столбца
            if i == j :                    #Проверка диагонали
                result_diagonal_left += array[i][j]
            if i==1 and j==1:
                result_diagonal_right += array[i][j]
            if i==2 and j==0:
                result_diagonal_right += array[i][j]
            if i==0 and j==2:
                result_diagonal_right += array[i][j]
        if result_line == 'XXX' or result_row == 'XXX' or result_diagonal_left == 'XXX' or result_diagonal_right == 'XXX':
            win = 'X'
        elif result_line == 'OOO' or result_row == 'OOO' or result_diagonal_left == 'OOO' or result_diagonal_right == 'OOO':
            win = 'O'
    return win


def start_game(row, line, table, char):
    row = int(row)
    line = int(line)
    table[line - 1][row - 1] = char
    return
    # if chek_win(table) == 'O' or chek_win(table) == 'X':
    #     print_array(table)
    #     print(f'Победили {chek_win(table)}')
    #     break

# print(creat_array())
