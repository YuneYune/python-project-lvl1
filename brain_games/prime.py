#!/usr/bin/env python3

"""Even commands."""

import sys
from random import SystemRandom

import prompt


def welcome_user():
    """Greeting.

    Returns:
        Returns name of the player
    """
    name = prompt.string('May I have your name? ')
    sys.stdout.write('Hello, {0}!\n'.format(name))
    return name


def define_rules():
    """Rules of the game."""
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'
    sys.stdout.write(rules)


def is_prime(number):
    """Check is num prime.

    Args:
        number: the number.

    Returns:
        Returns 'yes' or 'no'.
    """
    start = int(number / 2)
    for num in range(start, 1, -1):
        if number % num == 0:
            return 'no'
    return 'yes'


def question(*args):
    """Ask the question to the player.

    Args:
        args: numbers (int) and/or operator (str).

    Returns:
        Returns answer of the player.
    """
    message_with_symb = 'Question: {0}\n'.format(*args)
    sys.stdout.write(message_with_symb)
    return prompt.string('Your answer: ')


def game(name, amount_of_rounds=3):
    """One round of a game.

    Args:
        name: name of player.
        amount_of_rounds: how many rounds the game will continue.

    Returns:
        Returns nothing or recursively itself.
    """
    if amount_of_rounds <= 0:
        return sys.stdout.write('Congratulations, {0}!\n'.format(name))
    cryptogen = SystemRandom()
    number = cryptogen.randrange(100)
    answer = question(number)
    if answer == is_prime(number):
        sys.stdout.write('Correct!')
        return game(name, amount_of_rounds - 1)
    else:
        message = "'{0}' is wrong answer ;(. Correct answer was '{1}'\n"
        sys.stdout.write(message.format(answer, is_prime(number)))
        sys.stdout.write("Let's try again, {0}!\n".format(name))
