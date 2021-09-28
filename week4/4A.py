number  = int(input())

if number > 0:
    if number % 2 == 1:
        print("O")
    else:
        print("E")
else:
    if number == 0:
        print("Z")
    else:
        print("M")
