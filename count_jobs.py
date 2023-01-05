def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    ans = 0
    for i in data:
        for l,k in i.items():
            if k == job:
                ans += 1

    return ans 
print(count_jobs([{'name': 'John', 'job': 'Developer'}, {'name': 'Mary', 'job': 'Developer'}],"Developer"))
     