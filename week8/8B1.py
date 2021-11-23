dividend = list(map(int,input().split()))
n = int(input())

ans = 1

for e in dividend:
    ans *= (e % n)
    ans %= n

print(ans)
