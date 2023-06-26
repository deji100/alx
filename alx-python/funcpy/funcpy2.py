def hi(x):
    print("Hi I'm {}!".format(x.name))

class Robot:
    say_hi = hi

r1 = Robot()
r1.name = "Marvin"

Robot.say_hi(r1)