class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Student(Person):

    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        self.id = id

    def printInfo(self):
        print({'name': self.name, 'age': self.age, 'id': self.id})

s = Student("Deji", 25, 12345)
print(s.printInfo())