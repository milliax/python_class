import math

all = input().split()

new = []
for i in all:
    if all != "":
        new.append(int(i))

bar = 0.0

for i in new:
    bar += i
bar /= len(new)

total = 0

for i in new:
    total += (i-bar)*(i-bar)

ans = math.sqrt(total/len(new))

print("{:.3f}".format(ans))