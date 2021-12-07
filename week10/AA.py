a = int(input())

ans = 0.0

for i in range(1,a+1):
    ans += 1/i

print("{:.4f}".format(ans))