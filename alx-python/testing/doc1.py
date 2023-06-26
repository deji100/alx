"""
>>> my_function(3, 3)
9
"""

def my_function(a, b):
    """
    Returns a * b

    >>> my_function(2, 3) #doctest: +NORMALIZE_WHITESPACE
    6 

    and string

    >>> my_function('a', 3)
    'aaa'

    >>> name = "Deji"
    >>> 'name' in globals()
    True
    
    """
    name = "Deji"

    return a * b


if __name__ == "__main__":
    print(my_function(2, 3))