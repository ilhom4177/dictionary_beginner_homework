def get_user_country(data:list, name:str) -> list:
    """
    Return the country of a user with a given name

    Args:
        data (dict): A dictionary of values
        name (str): The name of the user to search for
    Returns:
        str: The country of the user with the given name
    """
    name1 = data[0]['name']
    name2 = data[1]['name']
    if name == name1:
        return data[0]['country']
    elif name == name2:
        return data[1]['country']
print(get_user_country([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}],"John"))
    