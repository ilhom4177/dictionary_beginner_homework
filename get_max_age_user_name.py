def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    age1 = data[0]['age']
    age2 = data[1]['age']
    if age1 > age2:
        return data[0]['name']
    else:
        return data[1]['name']
print(get_max_age_user_name([{'name': 'John', 'age': 29}, {'name': 'Mary', 'age': 2}]))