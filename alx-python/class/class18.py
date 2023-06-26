"""Defines A Rectangle class"""


class Rectangle:
    """Defines a Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance
        
        arguments:
            width: sets an instance width to default 0
            height: sets an instance height to default 0
        """

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of an instance"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets a new value to an instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of an instance"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets a new value to an instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
        
    def area(self):
        """Returns the area of a rectangle instance"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectangle instance"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.width)
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        
        return rect_2
    
    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
    
    def __str__(self):
        """Print the rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        
        for i in range(self.__height - 1):
            if self.print_symbol:
                print(str(self.print_symbol) * self.__width)
            else:
                print(str(Rectangle.print_symbol) * self.__width)

        if self.print_symbol:
            return str(self.print_symbol) * self.__width
        
        return str(Rectangle.print_symbol) * self.__width
    
    def __repr__(self):
        """Return a string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        """Prints a message after an instance is deleted"""

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

rec = Rectangle(3, 4)

print(rec.area())
print(rec.square(5))


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()