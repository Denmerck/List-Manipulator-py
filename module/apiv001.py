"""Api for DatMgrLib"""
def merge(TargetA: list | tuple | dict | set, TargetB: list | tuple | dict | set) -> list | tuple | dict | set:
    """merge(TargetA: list | tuple | dict | set, TargetB: list | tuple | dict | set)

    Merges 2 objects into a single object

    Parameters
    ----------
    TargetA : list, tuple, dict, or set to merge with.
    TargetB : list, tuple, dict, or set to merge to.
    """
    try:
        if type(TargetA) != type(TargetB):
            raise TypeError
    except TypeError:
        print("Both arguments are different types: TargetA. " + str(type(TargetA)) + " TargetB: " + str(type(TargetB)))
    else:
        typ = type(TargetA)
        if typ == list:
            return TargetA + TargetB
        elif typ == dict:
            a: dict = TargetA.copy()
            a.update(TargetB)
            return a
        elif typ == set:
            a: set = TargetA.copy()
            for i in TargetB:
                a.add(i)
            return a
        else:
            a: list = list()
            for i in TargetA:
                a.append(i)
            for i in TargetB:
                a.append(i)
            return tuple(a)

    

def removeduplicates(Target: list | tuple) -> list | tuple:
    """removeduplicates(Target: list | tuple | dict | set)

    Removes duplicate items.

    Parameters
    ----------
    Target : list, tuple, dict, or set to remove duplicates.
    """
    a = []
    if type(Target) == list:
        b = Target.copy()
        Target.reverse()
        for i in b: 
            if a.__contains__(i):
                Target.remove(i)
            else:
                a.append(i)
        Target.reverse()
        return Target
    if type(Target) == tuple:
        c = []
        for i in Target:
            if not a.__contains__(i):
                c.append(i)
                a.append(i)
        return tuple(c)

def remove(Target: list | tuple | set, element):
    """remove(obj: list | tuple | set, element)
    
    Remove an element from the contents.

    Parameters
    ----------
    Target : list, tuple or set.
    element : Value to be removed.
    """
    typ = type(Target)
    if typ == tuple:
        a = list(Target)
        a.remove(element)
        return tuple(a)

def differ(TargetA: list | tuple | set, TargetB: list | tuple | set) -> list | tuple | set:
    a = []
    b = []
    typA = type(TargetA)
    typB = type(TargetB)
    try:
        if typA != typB:
            raise TypeError
    except TypeError:
        print("Both arguments are different types: TargetA. " + str(type(TargetA)) + " TargetB: " + str(type(TargetB)))
    else:
        #Code goes here

__all__ = ["merge","removeduplicates","remove","differ"]