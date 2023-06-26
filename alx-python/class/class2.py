class Robot:

    population = 0

    def __init__(self, name) -> None:
        self.name = name

        print("Initializing {}".format(self.name))

        Robot.population += 1


    def die(self):
        """I'm a robot"""

        print("{} is being destroyed.".format(self.name))
        print()

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last robot destroyed.".format(self.name))
            print()
        elif Robot.population == 1:
            print("We have {} last robot left".format(Robot.population))
            print()
        else:
            print("We have {} robots left".format(Robot.population))
            print()

    def say_hi(self):
        """Say hi"""
        print("Hello, my master named me {}".format(self.name))
        print()

    @classmethod
    def how_many(cls):
        """Prints how many robots exists."""
        print("We have {:d} robots left".format(cls.population))
        print()


r1 = Robot("Deji")
r1.say_hi()
Robot.how_many()


r2 = Robot("Segun")
r2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print()

print("Robots have finished their work. So let's destroy them.")
print()
r1.die()
r2.die()

Robot.how_many()
print()
print(r1.__dict__)
print()
print(r2.__dict__)

