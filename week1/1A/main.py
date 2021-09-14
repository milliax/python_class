arr = []
sum = 0

for i in range(5):
    arr.append(int(input()))
    sum += arr[i]

print("sum:%d" % sum)
sum = float(sum)
print("avg:%.2f" % (sum/5))