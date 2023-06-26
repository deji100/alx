class SchoolMember:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

        print("Initializing SchoolMember: {}".format(self.name))

    def tell(self):
        print("Name: {}, Age: {}".format(self.name, self.age), end=" ")

class Teacher(SchoolMember):

    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age)
        self.salary = salary

        print("Initializing Teacher {}".format(self.name))

    def tell(self):
        super().tell()
        print("Salary: {}".format(self.salary), end="")
        return ""

    def __str__(self) -> str:
        return self.name

class Student(SchoolMember):

    def __init__(self, name, age, marks) -> None:
        super().__init__(name, age)
        self.marks = marks

        print("Initializing Student: {}".format(self.name))

    def tell(self):
        super().tell()
        print("Marks: {}".format(self.marks), end= "")

        return ""

    def __str__(self) -> str:
        return self.name

t = Teacher("Mrs. Adeyemi", 30, 500000)
print(t.tell())
print()

s = Student("Jumoke", 19, 90)
print(s.tell())