arr = input().split()

lonely = []

for e in arr:
    if e in lonely:
        lonely.remove(e)
    else:
        lonely.append(e)

print(*lonely,sep=" ")