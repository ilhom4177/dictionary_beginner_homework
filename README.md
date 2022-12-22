# Welcome
# Dictionary

Automated grading of homework assignments and tests
- fork this repository
- solve the task
- commit with proper message

# Problems
## count_jobs

  Return the number of users with a given job.

**Example 1:**

```Python
Input: 
data=[
  {
    'name': 'John', 
    'job': 'Developer'
  }, 
  {
    'name': 'Mary', 
    'job': 'Developer'
  }
  ]

job = 'Developer'
  
Output: 2

```
**Example 2:**

```Python
Input: 
data = [
  {
    'name': 'John',
    'job': 'Barber'
  }, 
  {
    'name': 'Mary',
    'job': 'Developer'
  },
  {
    'name': 'Ann', 
    'job': 'Teacher'
  }
  ]
job = "Student"
Output: 0

```
**Constraints:**
  - 0 <= len(data) <= 10^5
  - 0 <= len(job) <= 10^5

## count_users_with_age

  Return the number of users with a given age.

**Example 1:**

```Python
Input: data = [
  {
    'name': 'John',
    'age': 27
  },
  {
    'name':'Mary', 
    'age': 42
  },
  {
    'name':'Ann',
    'age': 27
  }
  ]
age = 27
Output: 2
```
**Example 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 35
  },
  {
    'name':'Mary', 
    'age': 20
  }
  ]
age = 38
Output: 0

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= age <= 10^5

## find_int_keys

  Return a list of all keys in a dictionary that are integers.

**Example 1:**

```Python
Input: data = {
    'a': 1, 
    3 : 2, 
    'c': 3,
    10:'a'
  }
Output: [3, 10]

```
**Example 2:**

```Python
Input: data = {
    "x": "23",
    "3": "y", 
    "z": "5", 
    7:'a'
  }
Output: [7]

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## find_length_of_values

  Return the sum of the length of all values in a dictionary.

**Example 1:**

```Python
Input: data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }
Output: 9

```

**Example 2:**

```Python
Input: data = {
    1 : "Khiva", 
    2 : "Namangan", 
    3 : "Samarkand", 
    4 : "Tashkent"
  }
Output: 30

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## find_max_key

  Return the maximum key in a dictionary.

**Example 1:**

```Python
Input: data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }
Output: 3

```
**Example 2:**

```Python
Input: data = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  }
Output: 7.8

```
  - 0 <= len(data) <= 10^5

## find_max_value

  Return the maximum value in a dictionary.

**Example 1:**

```Python
Input: data = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  }
Output: 3

```
**Example 2:**

```Python
Input: data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }
Output: 0

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## get_max_age_user_name

  Return the name of the user with the maximum age in a dictionary.

**Example 1:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
Output: 'Mary'

```
**Example 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  }, 
  {
    'name': 'Ban', 
    'age': 29
  }
]
Output: 'John'

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## get_min_age_user_name

  Return the name of the user with the minimum age in a dictionary.

**Example 1:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
Output: 'John'

```
**Example 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  },
  {
    'name': 'Ban', 
    'age': 29
  }
]
Output: 'Mary'

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## get_user_country

  Return the country of a user with a given name.

**Example 1:**

```Python
Input: data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  }
]
name = "John"
Output: 'USA'
```
**Example 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  },
  {
    'name': 'Henry', 
    'country': 'UK'
  },
  {
    'name': 'Sam', 
    'country': 'MEX'
  },
  {
    'name': 'Kevin', 
    'country': 'RUS'
  },
  {
    'name': 'Dustin', 
    'country': 'GER'
  }
]
name = "Henry"
Output: 'UK'

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= len(name) <= 10^5

## get_user_names_with_age_range

  Return a list of users with a given age range

**Example 1:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
]
min_age = 18
max_age = 25
Output: ['John','Ban']

```
**Example 2:**

```Python
Input: data = [
  {
    'name': 'Anny', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 30
  }
]
min_age = 20
max_age = 30
Output: ['Anny','Mary']

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= max_age <= 10^5
  - 0 <= min_age <= 10^5

## get_user_names_with_age

  Return a list of users with a given age

**Example 1:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
age = 27
Output: ['John']

```
**Example 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 30
  }, 
  {
    'name': 'Ann', 
    'age': 32
  }, 
  {
    'name': 'Sam', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 32
  }
]
age = 32
Output: ['Ann','Mary']

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= age <= 10^5

## get_user_names

  Return a list of users with a given country

**Example 1:**

```Python
Input: data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  }
]
country = "USA"
Output: ["John"]

```
**Example 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  },
  {
    'name': 'Henry', 
    'country': 'UK'
  },
  {
    'name': 'Sam', 
    'country': 'MEX'
  },
  {
    'name': 'Kevin', 
    'country': 'RUS'
  },
  {
    'name': 'Dustin', 
    'country': 'GER'
  }
]
country = 'UK'
Output: ["Mary","Henry"]

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= len(country) <= 10^5

## sum_age_values

  Return the sum of all age values in a dictionary.

**Example 1:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
Output: 69

```
**Example 2:**

```Python
Input: data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
]
Output: 87

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## sum_dict_values

  Return the sum of all values in a dictionary.

**Example 1:**

```Python
Input: data = {
    'a': 1, 
    'b': 2, 
    'c': 3
  }
Output: 6

```
**Example 2:**

```Python
Input: data = {
    1: 23, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }
Output: 39.5

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## sum_even_values

  Return the sum of all even values in a dictionary.
  
**Example 1:**

```Python
Input: data = {
    'a': 1, 
    'b': 2, 
    'c': 3
  }
Output: 2

```
**Example 2:**

```Python
Input: data = {
    1: 22, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }
Output: 24

```

**Constraints:**

  - 0 <= len(data) <= 10^5

## sum_float_values

  Return the sum of all float values in dictionary.

**Example 1:**

```Python
Input: data = {
    'a': 1, 
    'b' : 2.5, 
    'c': 3.0
  }
Output: 5.5

```
**Example 2:**

```Python
Input: data = {
    1: 22.4, 
    2: 3.5, 
    4: 1, 
    6: 7.6, 
    5: 2, 
    7: 3
  }
Output: 33.5

```

**Constraints:**

  - 0 <= len(data) <= 10^5

# Warning
- don't copy other solutions or any solution
- don't remove comments