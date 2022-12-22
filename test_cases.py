## count_jobs
'''**Example 1:**

```Python
Input: ([{'name': 'John', 'job': 'Developer'}, {'name': 'Mary', 'job': 'Developer'}],"Developer")
Output: 2

```
**Example 2:**

```Python
Input: ([{'name': 'John', 'job': 'Barber'}, {'name': 'Mary', 'job': 'Developer'},{'name': 'Ann', 'job': 'Teacher'}],"Student")
Output: 0
```
**Example 3:**

```Python
Input: ([{'name': 'John', 'job': 'Barber'}, {'name': 'Mary', 'job': 'Developer'},{'name': 'Ann', 'job': 'Teacher'}],"Teacher")
Output: 1
```
'''
## count_users_with_age
"""
**Example 1:**

```Python
Input: ([{'name': 'John', 'age': 27},{'name':'Mary', 'age': 42},{'name':'Ann', 'age': 27}],27)
Output: 2
```
**Example 2:**
```Python
Input: ([{'name': 'John', 'age': 35},{'name':'Mary', 'age': 20}],38)
Output: 0

```
"""
## find_int_keys
"""
**Example 1:**

```Python
Input: {'a': 1, 3: 2, 'c': 3,10:'a'}
Output: [3, 10]

```
**Example 2:**

```Python
Input: {"x": "23", "3": "y", "z": "5", 7:'a'}
Output: [7]

```
**Example 3:**

```Python
Input: {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
Output: []

```
"""
## find_length_of_values
"""
**Example 1:**

```Python
Input: {'a': 'abc', 'b': 'def', 'c': 'ghi'}
Output: 9

```

**Example 2:**

```Python
Input: {1: "Khiva", 2: "Namangan", 3: "Samarkand", 4: "Tashkent"}
Output: 30

```
**Example 3:**

```Python
Input: {1: "", 2: "", 3: "", 4: ""}
Output: 0

```
"""

## find_max_key

"""
**Example 1:**

```Python
Input: {1:'a', 2:'b', 3: 'c'}
Output: 3

```
**Example 2:**

```Python
Input: {1.4:'a', 7.8:'b', 4: 'c'}
Output: 7.8

```
**Example 3:**

```Python
Input: {0:'a', -1:'b', 2: 'c'}
Output: 2
"""
## find_max_value
"""
**Example 1:**

```Python
Input: {'a': 1, 'b': 2, "c" : 3}
Output: 3

```
**Example 2:**

```Python
Input: {'a': -4, 'b': -10, "c" : 0}
Output: 0
```
**Example 3:**

```Python
Input: {'a': -2.5, 'b': 3.2, "c" : 7.1}
Output: 7.1
```
"""

## get_country_with_least_users
"""
**Example 1:**

```Python
Input: [{'name': 'Ann', 'country': 'USA'},{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]
Output: 'USA'

```
**Example 2:**

```Python
Input: [{'name': 'Ann', 'country': 'USA'},{'name': 'John', 'country': 'UK'}]
Output: 'USA'

```
**Example 3:**

```Python
Input: [{'name': 'Ann', 'country': 'USA'},{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'},{'name': 'Henry', 'country': 'UK'},{'name': 'Sam', 'country': 'UK'},{'name': 'Kevin', 'country': 'UK'},{'name': 'Dustin', 'country': 'UK'},{'name': 'Sally', 'country': 'UZ'}]
Output: 'UZ'

```
"""

## get_country_with_most_users
"""
**Example 1:**

```Python
Input:[{'name': 'John', 'country': 'USA'},{'name': 'Walker', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]
Output: "USA"

```
```
**Example 2:**

```Python
Input: [{'name': 'Ann', 'country': 'USA'},{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'},{'name': 'Henry', 'country': 'UK'},{'name': 'Sam', 'country': 'UK'},{'name': 'Kevin', 'country': 'UK'},{'name': 'Dustin', 'country': 'UK'},{'name': 'Sally', 'country': 'UZ'}]
Output: "UK"

```
"""
## get_max_age_user_name
"""
**Example 1:**

```Python
Input: [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
Output: 'Mary'

```
**Example 2:**

```Python
Input: [{'name': 'John', 'age': 32}, {'name': 'Mary', 'age': 18}, {'name': 'Ann', 'age': 20}, {'name': 'Ban', 'age': 29}]
Output: 'John'

```
**Example 3:**

```Python
Input: [{'name': 'John', 'age': 25}, {'name': 'Mary', 'age': 25}]
Output: 'John'

```
"""
## get_min_age_user_name
"""
**Example 1:**

```Python
Input: [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
Output: 'John'

```
**Example 2:**

```Python
Input: [{'name': 'John', 'age': 32}, {'name': 'Mary', 'age': 18}, {'name': 'Ann', 'age': 20}, {'name': 'Ban', 'age': 29}]
Output: 'Mary'

```
**Example 3:**

```Python
Input: [{'name': 'John', 'age': 25}, {'name': 'Mary', 'age': 25}]
Output: 'John'

```
"""

## get_user_country
"""
**Example 1:**

```Python
Input: ([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}],"John")
Output: 'USA'

```
**Example 2:**

```Python
Input: ([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'},{'name': 'Henry', 'country': 'UK'},{'name': 'Sam', 'country': 'MEX'},{'name': 'Kevin', 'country': 'RUS'},{'name': 'Dustin', 'country': 'GER'}],"Henry")
Output: 'UK'

```
**Example 3:**

```Python
Input: ([{'name': 'Ann', 'country': 'USA'},{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'},{'name': 'Henry', 'country': 'UK'},{'name': 'Sam', 'country': 'MEX'},{'name': 'Kevin', 'country': 'RUS'},{'name': 'Dustin', 'country': 'GER'},{'name': 'Anvar', 'country': 'UZ'}],"Anvar")
Output: 'UZ'

```
"""
## get_user_names_with_age_range
"""
**Example 1:**

```Python
Input: ([{'name': 'John', 'age': 20}, {'name': 'Mary', 'age': 17},{'name': 'Ban', 'age': 23},{'name': 'John', 'age': 27}],18,25)
Output: ['John','Ban']

```
**Example 2:**

```Python
Input: ([{'name': 'Anny', 'age': 20}, {'name': 'Mary', 'age': 30}],20,30)
Output: ['John','Mary']

```
**Example 3:**

```Python
Input: ([{'name': 'Anny', 'age': 20}, {'name': 'Ann', 'age': 30}, {'name': 'John', 'age': 11}, {'name': 'Mary', 'age': 27}],10,25)
Output: ['Anny','John']

```
"""
## get_user_names_with_age

'''
**Example 1:**

```Python
Input: ([{'name': 'John', 'age': 30},{'name': 'Sam', 'age': 27}, {'name': 'Mary', 'age': 42}],27)
Output: ['Sam']

```
**Example 2:**

```Python
Input: ([{'name': 'John', 'age': 30}, {'name': 'Ann', 'age': 32}, {'name': 'Sam', 'age': 27}, {'name': 'Mary', 'age': 32}],32)
Output: ['Ann','Mary']

```
**Example 3:**

```Python
Input: ([{'name': 'John', 'age': 20}, {'name': 'Ann', 'age': 20}, {'name': 'Sam', 'age': 20}, {'name': 'Mary', 'age': 20}],20)
Output: ['John','Ann','Sam','Mary']

```
**Example 4:**

```Python
Input: ([{'name': 'John', 'age': 20}, {'name': 'Ann', 'age': 20}, {'name': 'Sam', 'age': 20}, {'name': 'Mary', 'age': 20}],21)
Output: []

```
'''
## get_user_names
'''
**Example 1:**

```Python
Input: ([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}],"USA")
Output: ["John"]

```
**Example 2:**

```Python
Input: ([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}],"USA")
Output: ["John"]

```
**Example 2:**

```Python
Input: ([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'},{'name': 'Henry', 'country': 'UK'},{'name': 'Sam', 'country': 'MEX'},{'name': 'Kevin', 'country': 'RUS'},{'name': 'Dustin', 'country': 'GER'}],'UK')
Output: ["Mary","Henry"]

```
**Example 3:**

```Python
Input: ([{'name': 'Anvar', 'country': 'UZ'},{'name': 'Sardor', 'country': 'UZ'}, {'name': 'Mary', 'country': 'UK'},{'name': 'Henry', 'country': 'UK'},{'name': 'Sam', 'country': 'MEX'},{'name': 'Kevin', 'country': 'RUS'},{'name': 'Dustin', 'country': 'GER'},{'name': 'Ikrom', 'country': 'UZ'}],"UZ")
Output: ['Anvar','Sardor','Ikrom']

```
'''
## sum_age_values

'''
**Example 1:**

```Python
Input: [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
Output: 69

```
**Example 2:**

```Python
Input: ([{'name': 'John', 'age': 20}, {'name': 'Mary', 'age': 17},{'name': 'Ban', 'age': 23},{'name': 'John', 'age': 27}])
Output: 87

```

**Example 3:**

```Python
Input: ([{'name': 'John', 'age': 25}, {'name': 'Ann', 'age': 20}, {'name': 'Sam', 'age': 25}, {'name': 'Mary', 'age': 20}])
Output: 90


```
'''

## sum_dict_values
'''
**Example 1:**

```Python
Input: {'a': 1, 'b': 2, 'c': 3}
Output: 6

```
**Example 2:**

```Python
Input: {1: 23, 2: 3.5, 4: 1, 6: 7, 5: 2, 7: 3}
Output: 39.5

```
'''

## sum_even_values
''' 
**Example 1:**

```Python
Input: {'a': 1, 'b': 2, 'c': 3}
Output: 2

```
**Example 2:**

```Python
Input: {'a': 0, 'b': 8, 'c': 3}
Output: 8

```
**Example 3:**

```Python
Input: {1: 22, 2: 3.5, 4: 1, 6: 7, 5: 2, 7: 3}
Output: 24

```
'''
## sum_float_values
''' 
**Example 1:**

```Python
Input: {'a': 1, 'b': 2, 'c': 3}
Output: 0

```
**Example 2:**

```Python
Input: {'a': 0.5, 'b': 7.5, 'c': 3}
Output: 8

```
**Example 3:**

```Python
Input: {1: 22.4, 2: 3.5, 4: 1, 6: 7.6, 5: 2, 7: 3}
Output: 30.0

```
'''