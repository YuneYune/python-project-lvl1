#!/usr/bin/env python3

"""Brain game - add missing element of progression."""

import sys

from brain_games import prime


def main():
    """Algorithm."""
    sys.stdout.write('Welcome to the Brain Games!\n')
    name = prime.welcome_user()
    prime.define_rules()
    prime.game(name)


if __name__ == '__main__':
    main()
