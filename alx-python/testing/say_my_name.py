"""Defines a function with 
first_name and last name arguments
that returns <first name> <last name>
or raises a TypeError exception if
first_name and last_name are not strings"""


def say_my_name(first_name, last_name=""):
    """A function the validates arguments
    and returns a string <first_name> <last_name>"""

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))