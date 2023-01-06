def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    max = 0
    for i in data.keys():
        if max < i:
            max = i
    return max
print(find_max_key({1.4:'a', 7.8:'b', 4: 'c'})) 