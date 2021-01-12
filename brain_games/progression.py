#!/usr/bin/env python3

"""Even commands."""

import random
import re

import prompt

crypto = random.SystemRandom()


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
    print('What number is missing in the progression?')


def create_progression():
    """Create progression of numbers.

    Returns:
        Returns progression as a list.
    """
    progression = []
    begin = crypto.randrange(1, 100)
    step = crypto.randrange(1, 10)
    stop = step * 10 + begin
    for num in range(begin, stop, step):
        progression.append(str(num))
    return progression


def create_task():
    """Create 2 numbers and find the greatest common divisor of them.

    Returns:
        Returns progression of numbers and missing number.
    """
    progression = create_progression()
    index_of_missing = crypto.randrange(0, 10)
    missing = progression.pop(index_of_missing)
    progression.insert(index_of_missing, '..')
    return (progression, missing)


def question(*args):
    """Ask the question to the player.

    Args:
        *args: numbers (int) and/or operator (str).

    Returns:
        Returns answer of the player.
    """
    message_with_symb = 'Question: {0}'.format(*args)
    message = re.sub(r"[\[\,\'\]]", '', message_with_symb)
    print(message)
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
    (progression, missing_element) = create_task()
    answer = question(progression)
    if int(answer) == int(missing_element):
        print('Correct!')
        return game(name, amount_of_rounds - 1)
    else:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
            answer, missing_element,
        ),
        )
        print("Let's try again, {0}!".format(name))
