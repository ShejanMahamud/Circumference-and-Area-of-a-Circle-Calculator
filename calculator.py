#Circumference and Area of a Circle
import math
radius = float(input("Enter Radius of a Circle: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print("The Area Of Circle is:", round(area, 2))
print("The Circumference Of Circle is:", round(circumference, 2))
