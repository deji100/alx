class Robot:
    __counter = 0

    def __init__(self, name):
        self.name = name

        Robot.__counter += 1

    @classmethod
    def RobotInstances(cls):
        return cls.__counter

    
print(Robot.RobotInstances())
x = Robot("Jide")
print(x.RobotInstances())
