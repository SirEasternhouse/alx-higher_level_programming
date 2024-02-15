#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two intergers where b is set to a default number
    Args:
        param1: input and integer or float
        param2: default set to 98 , yet an interger or float may be inputed

    Return:
        the addtion of integer a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
