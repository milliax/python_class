a = float(input())
b = float(input())
c = float(input())

sum = a+b+c

if sum > 300 or sum < 0:
    print("BS")
else:
    if sum >= 180:
        print("PASS")
    else:
        print("FAIL")