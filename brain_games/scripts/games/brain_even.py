#!/usr/bin/env python3

"""Brain game - is number even."""

import sys

from brain_games import even


def main():
    """Algorithm."""
    sys.stdout.write('Welcome to the Brain Games!\n')
    name = even.welcome_user()
    even.define_rules()
    even.game(name)


if __name__ == '__main__':
    main()
