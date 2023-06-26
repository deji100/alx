#!/usr/bin/python3
"""Defines a square class inheriting from rectangle class"""
from rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(width, height, x, y, id)

    @property
    def size(self):
        """Returns the width or height of a square instance"""

        return self.width

    @size.setter
    def size(self, value):
        """Assign new value to the width and height of a square instance"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """Updates attrs of an instance"""

        if args and len(args) != 0:
            for i in args:
                if args.index(i) == 0:
                    self.id = args[0]
                elif args.index(i) == 1:
                    self.size = args[1]
                elif args.index(i) == 2:
                    self.x = args[2]
                else:
                    self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                else:
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary rep of a square instance"""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a str rep of a square instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"
