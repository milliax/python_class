n = int(input())
arr = input().split()

high = 0
low = 0

for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        high += 1
    elif arr[i] > arr[i+1]:
        low += 1

print("{}\n{}".format(high,low))
