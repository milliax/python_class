import math

arr = []
s = 0

for i in range(0,3):
    temp = input()
    arr.append(float(temp))
    s += arr[i]

s /= 2
ans = math.sqrt(s*(s-arr[0])*(s-arr[1])*(s-arr[2]))
print("{:.2f}".format(ans))