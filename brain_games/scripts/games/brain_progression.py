#!/usr/bin/env python3

"""Brain game - add missing element of progression."""

from brain_games import progression


def main():
    """Algorithm."""
    print('Welcome to the Brain Games!')
    name = progression.welcome_user()
    progression.define_rules()
    progression.game(name)


if __name__ == '__main__':
    main()
