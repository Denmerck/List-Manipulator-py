# Word "List" count: 164
"""
Library of list manipulation functions
"""

def subtract(A: list, B: list) -> list:
    """
    Removes the matching items\n
    eg.\n
        [a, b, c, d, d] - [a, c, e, d] = [a, b, d]

    :param A: Minuend
    :type A: list
    :param B: Subtrahend
    :type B: list
    """
    for i in A:
        if i in B:
            B.remove(i)
            A.remove(i)
    return A

def subtractboth(A: list, B: list) -> list:
    """
    Removes the matching items then passes the remaining.\n
    eg.\n
        [a, b, c, d, d] - [a, c, e, d, u] = [a, b, d, u]
    :param A: Minuend
    :type A: list
    :param B: Subtrahend
    :type B: list
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
    Merges (or removes) duplicates in a list.\n
    eg.\n
        [13, 64, "Nine", "Nine", "Holt"] -> [13, 64, "Nine", "Holt"]
    
    :param A: Target list
    :type A: list
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
    Flattens list that contains a list as its child.\n
    *Only affects the target list's child\n
    eg.\n
        [23, 95, ["Peralta", "76", True], "Manila"] -> [23, 95, "Peralta", "76", True, "Manila"]

    :param A: Target list
    :type A: list
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

def killitems(A: list, value: any) -> list:
    """
    Removes all occcurrences of a value in a list.\n
    eg.\n
        ["Non", "Non", "NUL", "Few"] -> ["NUL", "Few"]
    
    :param A: Target list
    :type A: list
    :param value: Value(s) to be cleared off
    :type value: any
    """
    cacheA = A.copy()
    for i in cacheA:
        if i == value:
            A.remove(i)
    return A

def replace(A: list, index: int, value: any) -> list:
    """
    Replaces the index with the value\n
    eg.\n
        ["Barbershop", "Haircut", "Cost", "Dollar"] -> ["Barbershop", "Haircut", "Cost", "Quarter"]
    
    :param A: Target list
    :type A: list
    :param index: Index to replace
    :type index: int
    :param value: Replacement Value
    :type value: any
    """
    A.pop(index)
    A.insert(index, value)
    return A

def replaceitems(A: list, target: any, value: any) -> list:
    """
    Replaces all occurrence of target with the value\n
    eg.\n
        ["Loblaws", "Loblaws", "Canadia", "Loblaws", "Chat"] ->\n["CityMarket", "CityMarket", "Canadia", "CityMarket", "Chat"]
    
    :param A: Target
    :type A: list
    :param target: Description
    :type target: any
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