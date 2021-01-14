#!/usr/bin/env python3

"""Cli commands."""

import sys

import prompt


def welcome_user():
    """Greeting."""
    name = prompt.string('May I have your name? ')
    sys.stdout.write('Hello, {0}!\n'.format(name))
