"""
PyCodeStyle with PEP 8
PEP 8: https://www.python.org/dev/peps/pep-0008/

https://code.visualstudio.com/docs/python/linting#_specific-linters

Python:Select Linter

Usage:
pycodestyle --first src/linting.py
pycodestyle --show-source --show-pep8 src/linting.py
"""


def ThisIsAFunction(name):
    print(f'Hello {name}!')


def main():
    name = 'Spock'
    print(f'Hello {name}!')


if __name__ == "__main__":
    main()
