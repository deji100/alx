class Robot:

    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name != None:
            print("Hi, I'm {}!".format(self.name))
        else:
            print("Hi, my maker created me without a name.")

    def set_name(self):
        self.name = "Deji"

    def get_name(self):
        return self.name

    def __repr__(self) -> str:
        return "Robot " + self.name + " was built in the year " + str(self.build_year)

    def __str__(self) -> str:
        return "Robot Name: {name}, Build Year: {year}".format(name=self.name, year=self.build_year)

r = Robot("Marvin", 1997)
r1 = Robot()

r.say_hi()
# r1.say_hi()
# r_name = r.get_name()
# print(r_name)
# r.set_name()
# print(r.name)
# print(str(r))
str_r = repr(r)
print(str_r)
print("Type of str_r is {}".format(type(str_r)))
# new = eval(str_r)
# print(new)
# print("Type of new is {}".format(type(new)))

    