ans = set()
lines = 0

while True:
    try:
        new = input().split(",")
        ans.add(e for e in new)
        lines += 1
    except:
        break

print(lines-1)
print(list(ans))