#!/usr/bin/env python3

"""Brain game - is number even."""

from brain_games import even


def main():
    """Algorithm."""
    print('Welcome to the Brain Games!')
    name = even.welcome_user()
    even.define_rules()
    even.round(name)


if __name__ == '__main__':
    main()
