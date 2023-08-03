positions = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*']
    ]


def print_board():
    """Вывод доски для игры в крестики-нолики"""
    print("    0   1   2")
    print("  " + "-" * 13)
    for row in range(3):
        print(row, end=" | ")
        for col in range(3):
            print(positions[row][col], end=" | ")
        print("\n  " + "-" * 13)


def check_draw():
    """Проверка на ничью"""
    result = True
    for i in range(3):
        for j in range(3):
            if positions[i][j] == '*':
                result = False
    return result


def check_game_over() -> bool:
    """Проверка, закончилась ли игра, входные данные positions, возврат True/False"""
    def check_line(a, b, c):
        return a == b == c and a in ('X', 'O')

    for i in range(3):
        if check_line(positions[i][0], positions[i][1], positions[i][2]):
            return True
        if check_line(positions[0][i], positions[1][i], positions[2][i]):
            return True

    if check_line(positions[0][0], positions[1][1], positions[2][2]):
        return True
    if check_line(positions[0][2], positions[1][1], positions[2][0]):
        return True

    draw = check_draw()
    if draw:
        return True

    return False


def player_input():
    """обработка ввода игрока"""
    valid_move = False

    while valid_move is not True:
        try:
            move = input('Введите координаты клетки куда хотите'
                         ' поставить ваш знак, через пробел, например "1 1"\n>')
            move = move.split()
            first_pos = int(move[0])
            second_pos = int(move[1])

            if first_pos in [0,1,2] and second_pos in [0,1,2]:
                valid_move = True
            else:
                raise ValueError

            if positions[first_pos][second_pos] != '*':
                print('Эта клетка уже занята, выберите другую')
                valid_move = False
        except:
            print('Неверный ввод, попробуйте еще раз')
    return first_pos, second_pos
