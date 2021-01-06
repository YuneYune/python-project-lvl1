#!/usr/bin/env python3

"""Even commands."""


from random import SystemRandom

import prompt


def define_rules():
    """Prints rules of the game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')


def welcome_user():
    """Greeting.

    Returns:
        Returns name of the player
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def is_even(num):
    """Check is num even or odd.

    Args:
        num: the number.

    Returns:
        Returns 'yes' or 'no'.
    """
    if num % 2:
        return 'no'
    return 'yes'


def round(name, amount_of_rounds=3):
    """One round of a game.

    Args:
        name: name of player.
        amount_of_rounds: how many rounds the game will continue.

    Returns:
        Returns nothing or recursively itself.
    """
    if amount_of_rounds <= 0:
        print('Congratulations, {0}!'.format(name))
    else:
        cryptogen = SystemRandom()
        number = cryptogen.randrange(100)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == is_even(number):
            print('Correct!')
            return round(name, amount_of_rounds - 1)
        else:
            message = ("'{0}' is wrong answer ;(. Correct answer was '{1}'.\n" +
                       "Let's try again, {2}!"
                       ).format(answer, is_even(number), name)
            print(message)
