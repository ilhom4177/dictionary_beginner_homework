def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    max = 0
    for i in data.values():
        if max < i:
            max = i
    return max
print(find_max_value({'a': 1, 'b': 12, "c" : 3}))