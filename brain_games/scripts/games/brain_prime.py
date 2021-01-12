#!/usr/bin/env python3

"""Brain game - add missing element of progression."""

from brain_games import prime


def main():
    """Algorithm."""
    print('Welcome to the Brain Games!')
    name = prime.welcome_user()
    prime.define_rules()
    prime.game(name)


if __name__ == '__main__':
    main()
