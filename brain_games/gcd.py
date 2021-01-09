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
            return divisor


def create_task():
    """Create 2 numbers and find the greatest common divisor of them.

    В такой реализации создания таски шанс того, что НОД != 1 или != 2 немногим
    меньше , как и НОД = 1 или = 2

    Returns:
        Returns 2 numbers and the greatest common divisor of them.
    """
    main = crypto.randrange(1, 11)  # noqa: WPS432
    num1 = main * crypto.randrange(1, 10)
    num2 = main * crypto.randrange(1, 10)
    return (num1, num2, find_gcd(num1, num2))


def question(*args):
    """Ask the question to the player.

    Args:
        *args: numbers (int) and/or operator (str).

    Returns:
        Returns answer of the player.
    """
    print('Question: {0} {1}'.format(args[0], args[1]))
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
    (first_num, second_num, gcd) = create_task()
    answer = question(first_num, second_num)
    if int(answer) == gcd:
        print('Correct!')
        return game(name, amount_of_rounds - 1)
    else:
        message = ("'{0}' is wrong answer ;(. Correct answer was '{1}'.\n" +
                   "Let's try again, {2}!"
                   ).format(answer, gcd, name)
        print(message)
