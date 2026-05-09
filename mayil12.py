import math

# Input values
a = 1
b = -5
c = 6

# Discriminant
d = (b**2) - (4*a*c)

# Solutions
x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print("Roots are:")
print("x1 =", x1)
print("x2 =", x2)
