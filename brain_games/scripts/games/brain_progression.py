#!/usr/bin/env python3

"""Brain game - add missing element of progression."""

import sys

from brain_games import progression


def main():
    """Algorithm."""
    sys.stdout.write('Welcome to the Brain Games!\n')
    name = progression.welcome_user()
    progression.define_rules()
    progression.game(name)


if __name__ == '__main__':
    main()
