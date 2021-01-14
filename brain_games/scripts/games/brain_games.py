#!/usr/bin/env python3

"""Main app."""

import sys

from brain_games import cli


def main():
    """Call functions."""
    sys.stdout.write('Welcome to the Brain Games!\n')
    cli.welcome_user()


if __name__ == '__main__':
    main()
