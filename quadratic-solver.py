import math

a = int(input("Give me the coefficient of x^2: "))

b = int(input('Give me the coefficient of x: '))

c = int(input('Give me the constant term: '))

root1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
root2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a

print("The only two solutions are:")
print(root1, "and", root2)
