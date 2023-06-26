class Robot:

    def __init__(self, name=None, build_year=None):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name != None:
            print("Hi, I'm {}!".format(self.__name))
        else:
            print("Hi, my maker created me without a name.")
        return ''

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self) -> str:
        return "Robot " + self.__name + " was built in the year " + str(self.__build_year)

    def __str__(self) -> str:
        return "Robot Name: {name}, Build Year: {year}".format(name=self.__name, year=self.__build_year)

r = Robot("Marvin", 1997)
r1 = Robot("Jide", 1980)

for x in [r, r1]:
    print(x.say_hi())
    if x.get_name() == "Jide":
        x.set_build_year(1985)
    print("I am {} and was built in the year {}".format(x.get_name(), x.get_build_year()))