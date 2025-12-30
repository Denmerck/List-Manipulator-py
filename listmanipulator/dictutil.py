"""
Library of dictionary manipulation functions
"""

def reversekeys(A: dict) -> dict:
    """
    Reverse the pairs of a dictionary. (Key <-> value)
    :param A: Target dict
    :type A: dict
    :return: Reversed dictionary
    """
    cacheA = A.copy()
    A.clear()
    for key, value in cacheA.items():
        A.update({key: value})
    return A