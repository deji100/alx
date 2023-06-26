class Robot:
    brand = 'kuka'

r1 = Robot()
r2 = Robot()
Robot.brand = "Kuka"

r1.brand = "Thales"

print(r1.brand)
print(Robot.brand)
print(r2.brand)
print(getattr(r1, 'energy', None))
