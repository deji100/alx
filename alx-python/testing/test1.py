"""Defines add_integer(a, b=98) function with
parameter a and b=98 that checks the types
and raises exception on the wrong types and
finally returns integer of the addition of 
a and b"""

def add_integer(a, b=98):
    """a: an integer or float arg
       b: a kargs with default value 98. Must be either int or float
       Returns an integer: the addition of a and b"""

    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    
    if type(a) is float or type(b) is float:
        a, b = int(a), int(b)
        return a + b
    else:
        return a + b