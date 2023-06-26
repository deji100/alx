def unpredictable(a):
    """
    >>> unpredictable(2) #doctest: +ELLIPSIS
    0x...
    """

    return id(a)