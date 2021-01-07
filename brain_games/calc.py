#!/usr/bin/env python3

"""Even commands."""

import random
from operator import add, mul, sub

import prompt

crypto = random.SystemRandom()
operators_as_str = ['+', '-', '*']


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
    print('What is the result of the expression?')


def question(num1, operator, num2):
    """Question to the player.

    Args:
        num1: first operand (int)
        operator: operator (str)
        num2: second operand (int).

    Returns:
        Returns answer of the player.
    """
    print('Question: {0} {1} {2}'.format(num1, operator, num2))
    return prompt.string('Your answer: ')


def calc(num1, operator, num2):
    """Calculate an expression.

    Args:
        num1: first operand (int)
        operator: operator (str)
        num2: second operand (int).

    Returns:
        Returns result of calc as a string.
    """
    operators = {'+': add,
                 '-': sub,
                 '*': mul,
                 }
    return str(operators[operator](num1, num2))


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
    num1, num2 = crypto.randrange(100), crypto.randrange(10)
    operator = crypto.choice(operators_as_str)
    answer = question(num1, operator, num2)
    calculation = calc(num1, operator, num2)
    if answer == calculation:
        print('Correct!')
        return game(name, amount_of_rounds - 1)
    else:
        message = ("'{0}' is wrong answer ;(. Correct answer was '{1}'.\n" +
                   "Let's try again, {2}!"
                   ).format(answer, calculation, name)
        print(message)
