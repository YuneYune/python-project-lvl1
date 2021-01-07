#!/usr/bin/env python3

"""Even commands."""

import random

import prompt

crypto = random.SystemRandom()


def define_rules():
    """Rules of the game."""
    print('Find the greatest common divisor of given numbers.')


def welcome_user():
    """Greeting.

    Returns:
        Returns name of the player
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def find_gcd(num1, num2):
    """Find the greatest common divisor of given numbers.

    Args:
        num1: first number (int)
        num2: second number (int).

    Returns:
        Returns the greatest common divisor as a string.
    """
    [less, bigger] = sorted([num1, num2])
    for divisor in range(less, 0, -1):
        if less % divisor == 0 and bigger % divisor == 0:
            return str(divisor)


def question(num1, num2):
    """Question to the player.

    Args:
        num1: first number (int)
        num2: second number (int).

    Returns:
        Returns answer of the player.
    """
    print('Question: {0} {1}'.format(num1, num2))
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
        return print('Congratulations, {0}!'.format(name))
    num1, num2 = crypto.randrange(100), crypto.randrange(100)
    answer = question(num1, num2)
    gcd = find_gcd(num1, num2)
    if answer == gcd:
        print('Correct!')
        return game(name, amount_of_rounds - 1)
    else:
        message = ("'{0}' is wrong answer ;(. Correct answer was '{1}'.\n" +
                   "Let's try again, {2}!"
                   ).format(answer, gcd, name)
        print(message)
