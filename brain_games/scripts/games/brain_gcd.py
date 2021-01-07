#!/usr/bin/env python3

"""Brain game - calculate the numbers."""

from brain_games import gcd


def main():
    """Algorithm."""
    print('Welcome to the Brain Games!')
    name = gcd.welcome_user()
    gcd.define_rules()
    gcd.game(name)


if __name__ == '__main__':
    main()
