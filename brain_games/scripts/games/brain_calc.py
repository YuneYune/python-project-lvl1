#!/usr/bin/env python3

"""Brain game - calculate the numbers."""

import sys

from brain_games import calc


def main():
    """Algorithm."""
    sys.stdout.write('Welcome to the Brain Games!\n')
    name = calc.welcome_user()
    calc.define_rules()
    calc.game(name)


if __name__ == '__main__':
    main()
