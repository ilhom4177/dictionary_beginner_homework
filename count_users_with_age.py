def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    a = 0
    for i in data:
        for l, k in i.items():
            if k == age:
                a += 1
    return a
print(count_users_with_age([{'name': 'John', 'age': 35},{'name':'Mary', 'age': 20}],38)) 