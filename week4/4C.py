a = float(input())

if a < 60:
    a *= 1.25

b = float(input())
if b < 60:
    b *= 1.25

c = float(input())

if c < 60:
    c *= 1.25

sum = a+b+c

if sum >= 180:
    print("Hmm")
else:
    print("PleaseGoToDieOneDie")