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

def merge(A: dict, key1: any, key2: any) -> dict:
    """
    Merge two dictionaries. (Key <-> value)
    :param A: Target dict
    :param key1: First key
    :param key2: Second key
    :return:
    """
    pass
    cacheA = A.copy()
