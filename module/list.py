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
    Removes all occurrence of a value in a list.\n

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

def zip(A: list, B: list) -> list:
    """
    Zips a list\n

    :param A: Target list
    :param B: Target list
    :type A: list
    :type B: list
    :return:
    """
    cacheA = list.copy(A)
    iterA = iter(cacheA)
    iterB = iter(B)
    print(iterA)
    lenA = len(A)
    lenB = len(B)
    A.clear()
    i = 0
    try:
        while i <= max(lenA, lenB):
            i += 1
            A.append([next(iterA), next(iterB)])
    except StopIteration:
        while True:
            try:
                A.append([next(iterA)])
            except StopIteration:
                try:
                    A.append([next(iterB)])
                except StopIteration:
                    return A
    return A

def snap(A: list, index: int) -> list:
    """
    Snaps a list in after index into 2 list.\n

    :param A: Target list
    :type A: list
    :param index: Snap position
    :type index: int
    :return: Snapped list
    """
    cacheA = list.copy(A)
    cacheB = []
    cacheC = []
    A.clear()
    for i in cacheA:
        if cacheA.index(i) <= index:
            cacheB.append(i)
        elif cacheA.index(i) > index:
            cacheC.append(i)
    A.append(cacheB)
    A.append(cacheC)
    return A

def push(A: list, *args: any) -> list:
    """
    Pushes values in the list\n
    :param A: Target list
    :type A: list
    :param args: values
    :type args: any
    :return: Pushed list
    """
    for i in args:
        A.append(i)
    return A

def mergelist(A: list, B: list) -> list:
    """
    Merges two lists, disposes duplicates\n
    :param A: Target list
    :type A: list
    :param B: Target list
    :type B: list
    :return: Merged list
    """
    for i in B:
        if i not in A:
            A.append(i)
    return A

def flood(A: list, amount: int, value: any) -> list:
    """
    Floods a list with values\n
    :param A: Target list
    :type A: list
    :param amount: Flood amount
    :type amount: int
    :param value: Flood value
    :type value: any
    :return: Flooded list
    """
    i = 0
    while i <= amount:
        A.append(value)
        i += 1
    return A

def wipe(A: list, amount: int | None = None) -> list:
    """
    Wipes a certain amount of items in a list, no amount value will wipe all contents.
    :param A: Target list
    :type A: list
    :param amount: Number of items to wipe
    :type amount: int
    :return: Wiped list
    """
    if amount == None:
        return []
    for i in range(amount):
        try:
            A.pop(-1)
        except IndexError:
            return []
    return A