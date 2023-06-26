from math import pi
import dis

class MagicClass:
    """Represents a MagicClass class."""

    def __init__(self, radius):
        """Initialize a MagicClass instance.

        argument:
            radius:The radius of the new MagicClass instance.
        """
        
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of a MagicClass instance."""
        return ((self.__radius ** 2) * pi)

    def circumference(self):
        """Returns the circumference of a MagicClass instance."""
        return ((pi * 2) * self.__radius)


dis.dis(MagicClass)