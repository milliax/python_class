students = list(map(int,input().split()))

faint = 0

for e in students:
    if e == 0:
        faint += 1
    else:
        print(e,end=" ")

for i in range(faint):
    print(0,end=" ")

print()