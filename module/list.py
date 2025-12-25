# Word "List" count: 164
"""
Library of list manipulation functions
"""

def subtract(A: list, B: list) -> list:
    """
    Removes the matching items\n

    :param A: Minuend
    :type A: list
    :param B: Subtrahend
    :type B: list
    :return: Updated list
    """
    for i in A:
        if i in B:
            B.remove(i)
            A.remove(i)
    return A

def subtractboth(A: list, B: list) -> list:
    """
    Removes the matching items then passes the remaining.\n

    :param A: Minuend
    :type A: list
    :param B: Subtrahend
    :type B: list
    :return: Updated list
    """
    cacheA = list.copy(A)
    for i in cacheA:
        if i in B:
            print(True)
            B.remove(i)
            A.remove(i)
    return A + B

def mergeitems(A: list) -> list:
    """
    Merges (or removes) duplicate items in a list.\n
    
    :param A: Target list
    :type A: list

    :return: Updated list
    """

    cacheA = []
    cacheB = list.copy(A)
    for i in cacheB:
        if i in cacheA:
            A.remove(i)
        else:
            cacheA.append(i)
    return A

def flatten(A: list) -> list:
    """
    Pops all items in a child's list

    :param A: Target list
    :type A: list
    :return: Flattened list
    """

    cacheA = list.copy(A)
    A.clear()
    for i in cacheA:
        if type(i) == list:
            for ii in i:
                A.append(ii)
        else:
            A.append(i)
    return A

def killitems(A: list, *values) -> list:
    """
    Removes all occcurrences of a value in a list.\n
    
    :param A: Target list
    :type A: list
    :param value: Value(s) to be cleared off
    :type value: args
    :return: Updated list
    """
    cacheA = A.copy()
    for i in cacheA:
        if i in values:
            A.remove(i)
    return A

def replace(A: list, index: int, value: any) -> list:
    """
    Replaces the index with the value\n
    
    :param A: Target list
    :type A: list
    :param index: Index to replace
    :type index: int
    :param value: Replacement Value
    :type value: any

    :return: Updated list
    """
    A.pop(index)
    A.insert(index, value)
    return A

def replaceitems(A: list, target: any, value: any) -> list:
    """
    Replaces all items in a list

    :param A: Target list
    :type A: list
    :param target: Target item
    :type target: any
    :param value: Replacement Value
    :type value: any

    :return: Updated list
    """
    cacheA = list.copy(A)
    A.clear()
    for i in cacheA:
        if i == target:
            A.append(value)
        else:
            A.append(i)
    return A

# Module testing

testa = [1, 2, "Elanor", "Boyle", "Peralta"]
print(killitems(testa, "Boyle", "Peralta"))