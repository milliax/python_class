string = raw_input()

arr = string.split(" ")

total = 0

for i in range(2,7):
    total += float(arr[i])

print("{}: {:.4f}".format(arr[0],total/5))