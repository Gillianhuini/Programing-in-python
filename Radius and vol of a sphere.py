# write a python program that reads the radius of a sphere and calculates the volume.(Volume=4/3π³ ,use the math library to get pi,and give the answer into 2dps)
import math
radius = float(input("Enter the radius of the sphere: "))
volume = (4 / 3) * math.pi * (radius ** 3)
print("The volume of the sphere is:", round(volume, 2))
