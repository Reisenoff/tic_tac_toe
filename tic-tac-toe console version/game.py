"""
Игра крестики-нолики, консольная версия, 
только для двух игроков, автоматические 
ходы "компьютером" не предусмотрены
"""
from functions_for_tic_tac_toe import *


PLAYER_MOVE = 1


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
    end = input('Нажмите Enter для выхода') # При конвертации программы в exe не позволит закрыться сразу после завершения


if __name__ == '__main__':
    game()
