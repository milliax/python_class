length = int(input())

cost = 70

if length > 1500 and length <= 10000:
    length -= 1500
    times = 0
    while length > 0:
        length -= 500
        times += 1
    cost += times * 5
else:
    if length > 10000:
        cost = "Sleeping in school"
print(cost)
        