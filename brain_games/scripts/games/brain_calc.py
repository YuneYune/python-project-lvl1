#!/usr/bin/env python3

"""Brain game - calculate the numbers."""

from brain_games import calc


def main():
    """Algorithm."""
    print('Welcome to the Brain Games!')
    name = calc.welcome_user()
    calc.define_rules()
    calc.game(name)


if __name__ == '__main__':
    main()
