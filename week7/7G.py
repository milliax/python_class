# 輸入
row,column = list(map(int,input().split()))
x,y = list(map(int,input().split()))

floor = [False for i in range(row*column)]

steps = input().split()

#print(floor)

count = 0

for e in steps:
    count += 1
    #print("x: {},y: {}".format(x,y))
    
    floor[y * column + x] = True

    if not False in floor:
        break
    #print(floor)

    if e == '1':
        # going up
        if y != 0:
            y -= 1
        continue
    elif e == '2':
        if x != row -1:
            x += 1
        # going right
        continue
    elif e == '3':
        # going down
        if y != column -1:
            y += 1
        continue
    elif e == '4':
        # going left
        if x != 0:
            x -= 1
        continue

print(count)