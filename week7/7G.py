"""# 輸入
column,row = list(map(int,input().split()))
x,y = list(map(int,input().split()))

floor = [False for i in range(row*column)]

steps = input().split()

print(floor)

count = 0

for e in steps:
    print("x: {},y: {}".format(x,y))
    
    if not False in floor:
        break
    count += 1

    floor[x * column + y] = True
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

print(count)"""

m,n = list(map(int,input().split()))
y,x = list(map(int,input().split()))

floor = [False for i in range(m*n)]
#print(floor)

direction = input().split()
count = 0

"""
   m
   x ->
n  y | 1 | 2 | 3 |
   | | - | - | - |
   ^ | 4 | 5 | 6 |
     | 7 | 8 | 9 |

"""

for e in direction:
    #print(floor)
    if not False in floor:
        break
    count += 1
    print("d: {},x: {},y: {}".format(e,x,y))
    floor[y * m + x] = True


    if e == '1':
        # going up
        if not y == 0:
            y -= 1
        continue
    elif e == '2':
        # going right
        if not x == (m-1):
            x += 1
        continue
    elif e == '3':
        # going down
        if not y == (n-1):
            y += 1
        
        continue
    elif e == '4':
        # going left
        if not x == 0:
            x -= 1

        continue

print(count)