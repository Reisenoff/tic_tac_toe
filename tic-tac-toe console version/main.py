"""
Игра крестики-нолики, консольная версия, 
только для двух игроков, автоматические 
ходы "компьютером" не предусмотрены
"""
positions = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*']
    ]
PLAYER_MOVE = 1


def print_board():
    """Вывод доски для игры и дата файла"""
    print(f'  {"-"*13}\n0 | {positions[0][0]} | {positions[0][1]} | {positions[0][2]} |'
          f'\n  {"-"*13}\n1 | {positions[1][0]} | {positions[1][1]} | {positions[1][2]} |'
          f'\n  {"-"*13}\n2 | {positions[2][0]} | {positions[2][1]} | {positions[2][2]} |'
          f'\n  {"-"*13}\n    0   1   2')


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
    draw = check_draw()
    if positions[0][0] == positions[0][1] == positions[0][2] == ('X' or 'O'):
        return True
    elif positions[1][0] == positions[1][1] == positions[1][2] == ('X' or 'O'):
        return True
    elif positions[2][0] == positions[2][1] == positions[2][2] == ('X' or 'O'):
        return True
    elif positions[0][0] == positions[1][0] == positions[2][0] == ('X' or 'O'):
        return True
    elif positions[0][1] == positions[1][1] == positions[2][1] == ('X' or 'O'):
        return True
    elif positions[0][2] == positions[1][2] == positions[2][2] == ('X' or 'O'):
        return True
    elif positions[0][0] == positions[1][1] == positions[2][2] == ('X' or 'O'):
        return True
    elif positions[0][2] == positions[1][1] == positions[2][0] == ('X' or 'O'):
        return True
    elif draw is True:
        return True
    else:
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

        except:
            print('Неверный ввод, попробуйте еще раз')
    return first_pos, second_pos


def game():
    """Ядро игры"""
    game_over = False
    global PLAYER_MOVE, positions
    while game_over is not True:
        print_board()
        first_pos, second_pos = player_input()

        if PLAYER_MOVE == 1:
            positions[first_pos][second_pos] = 'X'
            PLAYER_MOVE = 2
        else:
            positions[first_pos][second_pos] = 'O'
            PLAYER_MOVE = 1

        game_over = check_game_over()
    draw = check_draw()
    if draw is True:
        winner = 'Ничья'
    elif PLAYER_MOVE == 1:
        winner = 'победа O'
    else: 
        winner = 'победа X'

    print_board()
    print(f'Игра завершена, {winner}')
    end = input('Нажмите Enter для выхода')

if __name__ == '__main__':
    game()