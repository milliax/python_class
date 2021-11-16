def show_map(floor,m):
    endl = m-1
    print("map")
    for i in range(len(floor)):
        if floor[i]:
            print("O",end=" ")
        else:
            print("X",end=" ")
        #print(floor[i],end=" ")
        if i == endl:
            print()
            endl += m

# 輸入
m,n = list(map(int,input().split()))
x,y = list(map(int,input().split()))

# 有 m*n 格地板
floor = [False for i in range(m*n)]

#老鼠的移動路徑
steps = input().split()

count = 0

for e in steps:
    count += 1
    floor[y * n + x] = True
    #show_map(floor,n)
    #print("d: {},x: {},y: {}".format(e,x,y))

    if not False in floor:
        break
    #print(floor)
    if e == '1':
        # going up
        if y != 0:
            y -= 1
        continue
    elif e == '2':
        # going right
        if x != (n - 1):
            x += 1
        continue
    elif e == '3':
        # going down
        if y != (m - 1):
            y += 1
        continue
    elif e == '4':
        # going left
        if x != 0:
            x -= 1
        continue

print(count)