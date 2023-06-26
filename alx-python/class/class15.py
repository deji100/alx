class DescriptorClass:

    def __init__(self, initval=None):
        print("Descriptor class initializes with ", initval)
        self.__set__(self, initval)

    def __get__(self):
        print("Retrieving self.val", self.val)
        return self.val
    
    def __set__(self, value) -> None:
        print("Setting self.__val to ", value)
        self.val = value

class Person:
    x = DeprecationWarning("Deji")

p = Person()
print(p.x)
p.x = "Jide"
print(p.x)