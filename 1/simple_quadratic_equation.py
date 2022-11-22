from math import sqrt

# ax^2 + bx + c = 0
a = float(input("enter a :"))
b = float(input("enter b :"))
c = float(input("enter c :"))

delta = b*b - 4*a*c

x1 = (-b+sqrt(delta)) / 2*a
x2 = (-b-sqrt(delta)) / 2*a

print(x1,x2) # x^2 + 2x + 1 = 0 => (x+1)^2 = 0 => x+1 = 0 => x=-1

