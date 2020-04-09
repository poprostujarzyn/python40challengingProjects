import math

print("Welcome to the Right Triangle Solver App\n")

a = float(input("What is the first leg of the triangle: "))
b = float(input("What is the second leg of the triangle: "))

c = round(math.sqrt(a**2 + b**2),3)
area = round((a * b / 2), 3)

print("For the Right Triangle with legs of %.3f and %.3f the hypotenuse is %.3f" %(a, b, c))
print("For the Right Triangle with legs of %.3f and %.3f the area is %.3f" %(a, b, area))
