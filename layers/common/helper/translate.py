def change_keys(obj, convert):
    """
Recursively goes through the dictionary obj and replaces keys with the convert function.
"""
    if isinstance(obj, (str, int, float)):
        return obj
    if isinstance(obj, dict):
        new = obj.__class__()
        for k, v in obj.items():
            if k in convert:
                new[convert[k]] = change_keys(v, convert)
            else:
                new[k] = change_keys(v, convert)
    elif isinstance(obj, (list, set, tuple)):
        new = obj.__class__(change_keys(v, convert) for v in obj)
    else:
        return obj
    return new
