#!/usr/bin/env python3

"""Even commands."""


from random import SystemRandom

import prompt


def welcome_user():
    """Greeting.

    Returns:
        Returns name of the player
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def define_rules():
    """Rules of the game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')


def question(*args):
    """Ask the question to the player.

    Args:
        *args: numbers (int) and/or operator (str).

    Returns:
        Returns answer of the player.
    """
    print('Question: {0} '.format(*args))
    return prompt.string('Your answer: ')


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


def game(name, amount_of_rounds=3):
    """One round of a game.

    Args:
        name: name of player.
        amount_of_rounds: how many rounds the game will continue.

    Returns:
        Returns nothing or recursively itself.
    """
    if amount_of_rounds <= 0:
        return print('Congratulations, {0}!'.format(name))
    cryptogen = SystemRandom()
    number = cryptogen.randrange(100)
    answer = question(number)
    if answer == is_even(number):
        print('Correct!')
        return game(name, amount_of_rounds - 1)
    else:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
            answer, is_even(number),
        ),
        )
        print("Let's try again, {0}!".format(name))
