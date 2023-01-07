def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    k=300
    for i in data:
        if k>i['age']:
            k=i['age']
            answer=i['name']
    return answer
print(get_min_age_user_name([{'name': 'John','age': 27},{'name': 'Mary','age': 42},{'name': 'Marra','age': 12}]))