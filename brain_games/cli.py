#!/usr/bin/env python3

"""Cli commands."""


import prompt


def welcome_user():
    """Greeting."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
