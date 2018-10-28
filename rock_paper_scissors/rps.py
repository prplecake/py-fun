# Rock, Paper, Scissors
# 21 July 2018
#
# By: Matthew Jorgensen
# matthew@jrgnsn.net
# https://jrgnsn.net
#
# Source code available at
# https://code.jrgnsn.net/matthew/py-rock-paper-scissors
#

import random


class Opponent:

    def __init__(self):
        self.__what = ''

    def randoms(self):
        digit = random.randint(0, 2)
        self.__what = ['rock', 'paper', 'scissors'][digit]

    def get_what(self):
        return self.__what


def eval_game(game1, game2):
    game_dict = {
        'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
        'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
        'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'},
    }
    result = game_dict[game1][game2]
    return result


def main():
    Op = Opponent()

    player_profit = 0
    computer_profit = 0

    print("""
Welcome to the game: Rock, Paper, Scissors!
Good luck out there,
Score goal: 3
Be my quest, start (rock, paper, scissors):
          """)
    while player_profit < 3 and computer_profit < 3:
        game = input('\t > ')

        Op.randoms()
        game2 = Op.get_what()

        if game in ['rock', 'paper', 'scissors']:
            print('\nYou picked: {}'.format(game), end='')
            print('\tI picked: {}\n'.format(game2))
        else:
            print('Input not found. You lose.')
            exit(1)

        result = eval_game(game, game2)
        if result == 'win':
            print('You win!')
            player_profit += 1
        elif result == 'tie':
            print('We tied...')
        elif result == 'lose':
            print('You lose!')
            computer_profit += 1

        print('\nYour score:\t{}\nMy score:\t{}'.format(player_profit,
                                                        computer_profit))
    if player_profit > computer_profit:
        print('\n\tYou won!!')
    elif player_profit < computer_profit:
        print('\n\tI won!!')


if __name__ == '__main__':
    main()
