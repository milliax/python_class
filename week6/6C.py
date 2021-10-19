total = 0.0
cnt = 0
passed = 0
original = []

while True:
    a = input()
    try:
        a = int(a)
        total += a
        cnt+=1
        original.append(a)
        if(a >= 60):
            passed += 1
    except:
        break

#passed
print(passed)
#failed
print(cnt-passed)
#average
print('{:.2f}'.format(total/cnt))
#sigma

average = total/cnt
added = 0.0

for i in range(cnt):
    added += (original[i]-average) ** 2

import math
added /= cnt

print("{:.2f}".format(math.sqrt(added)))
