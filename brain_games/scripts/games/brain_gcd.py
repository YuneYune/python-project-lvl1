#!/usr/bin/env python3

"""Brain game - calculate the numbers."""

import sys

from brain_games import gcd


def main():
    """Algorithm."""
    sys.stdout.write('Welcome to the Brain Games!\n')
    name = gcd.welcome_user()
    gcd.define_rules()
    gcd.game(name)


if __name__ == '__main__':
    main()
