"""
Library of dictionary manipulation functions
"""

def swap(A: dict) -> dict:
    """
    Reverse the pairs of a dictionary. (Key <-> value)
    :param A: Target dict
    :type A: dict
    :return: Reversed dictionary
    """
    cacheA = A.copy()
    A.clear()
    for key, value in cacheA.items():
        A.update({value: key})
    return A


def removevalue(A: dict, value: any) -> dict:
    """
    Remove a value from a dictionary.
    :param A: Target dict
    :param value: Value to remove
    :return:
    """
    for k, v in A.items():
        if v == value:
            A.pop(k)
    return A

def values(A: dict)-> list:
    """
    Get all values in a dictionary.
    :param A: Target dict
    :return:
    """
    values = []
    for k, v in A.items():
        values.append(v)
    return values

def keys(A: dict) -> list:
    """
    Get all keys in a dictionary.
    :param A: Target dict
    :return:
    """
    values = []
    for k, v in A.items():
        values.append(k)
    return values

def findvalue(A: dict, value: list) -> str:
    """
    Finds a value and returns a key.
    :param A: Target dict
    :param value: value to find
    :return:
    """
    for k, v in A.items():
        if v == value:
            return k
    return None
