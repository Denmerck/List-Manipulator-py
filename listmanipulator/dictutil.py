"""
Library of Dictionary Manipulation Functions
"""

def swap(Dict: dict) -> dict:
    """
    Swap the pairs of a dictionary. (Key <-> value)
    :param Dict: Target dict
    :type Dict: dict
    :return:
    """
    cacheDict = Dict.copy()
    Dict.clear()
    for key, value in cacheDict.items():
        Dict.update({value: key})
    return Dict


def removeValue(Dict: dict, value: any) -> dict:
    """
    Remove a value from a dictionary.
    :param Dict: Target dict
    :param value: Value to remove
    :return:
    """
    for k, v in Dict.items():
        if v == value:
            Dict.pop(k)
    return Dict

def values(Dict: dict)-> list:
    """
    Get all values in a dictionary.
    :param Dict: Target dict
    :return:
    """
    values = []
    for k, v in Dict.items():
        values.append(v)
    return values

def keys(Dict: dict) -> list:
    """
    Get all keys in a dictionary.
    :param Dict: Target dict
    :return:
    """
    values = []
    for k, v in Dict.items():
        values.append(k)
    return values

def findValue(Dict: dict, value: list) -> str:
    """
    Finds a value and returns a key.
    :param Dict: Target dict
    :param value: value to find
    """
    for k, v in Dict.items():
        if v == value:
            return k
    return None

def replaceKey(Dict: dict, TargetKey: any, Key: any) -> dict:
    """
    Replaces a key in a dictionary. returns with no modification if exact key is not found.
    :param Dict: Target Dict
    :param TargetKey: Target key
    :param Key: Replacement key
    """
    if TargetKey in Dict:
        ret = {Key: Dict[TargetKey]}
        Dict.pop(TargetKey)
        return Dict + ret
    else:
        return Dict

def flatten(Dict: dict) -> dict:
    """
    Unpacks a dictionary into its parent dictionary.
    :param Dict: Target Dict
    """
    for k, v in Dict:
        if type(v) == dict:
            for k, v in v:
                Dict.update({k: v})
            Dict.pop(k)
            return Dict
        else:
            return Dict

def toDict(List: list, Keys: list) -> dict:
    """
    Takes 2 list and merge them into a dictionary.

    :param List: List of items
    :param Keys: List of keys
    :return:
    """
    dict = {}
    for i in range(max(len(List), len(Keys))):
        dict.update({Keys[i]: List[i]})
    return dict