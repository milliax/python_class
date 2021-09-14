import math
a = float(input())
b = float(input())
c = float(input())

delta = b * b - 4 * a * c

print("{:.2f}".format((-b + math.sqrt(delta))/(a*2)))
print("{:.2f}".format((-b - math.sqrt(delta))/(2*a)))