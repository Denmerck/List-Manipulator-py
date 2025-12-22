"""
Set of functions for List
"""

def subtract(A: list, B: list):
    """
    # Subtract
    Removes the matching items\n
    eg.\n
        [a, b, c, d, d] - [a, c, e, d] = [a, b, d]

    :param A: Minuend
    :type A: List
    :param B: Subtrahend
    :type B: List
    """
    for i in A:
        if i in B:
            B.remove(i)
            A.remove(i)
    return A