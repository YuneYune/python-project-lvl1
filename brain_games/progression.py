#!/usr/bin/env python3

"""Even commands."""

import random
import re
import sys

import prompt

crypto = random.SystemRandom()


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
    sys.stdout.write('What number is missing in the progression?\n')


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
    r"""Ask the question to the player.

    Args:
        args: numbers (int) and/or operator (str).

    Returns:
        Returns answer of the player.
    """
    message_with_symb = 'Question: {0}\n'.format(*args)
    message = re.sub(r"[\[\,\'\]]", '', message_with_symb)
    sys.stdout.write(message)
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
    (progression, missing_element) = create_task()
    answer = question(progression)
    if int(answer) == int(missing_element):
        sys.stdout.write('Correct!\n')
        return game(name, amount_of_rounds - 1)
    else:
        message = "'{0}' is wrong answer ;(. Correct answer was '{1}'\n"
        sys.stdout.write(message.format(answer, missing_element))
        sys.stdout.write("Let's try again, {0}!\n".format(name))
