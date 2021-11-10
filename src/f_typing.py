"""
Illustration of Typing and Function Annotations
"""
import math


def greeting(name: str) -> str:
    """ Greet person with name
    """
    return f'Hello {name}'


def area(rad: float) -> float:
    """ Calculate area of a circle
    """
    return math.pi * rad * rad


def main():
    print(greeting('Seven of Nine'))
    print(area(2.45))


if __name__ == "__main__":
    main()
