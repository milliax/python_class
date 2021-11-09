def mul(number):
    numbers = str(number)
    numbers = list(numbers)
    total = 0
    for e in numbers:
        total += (int(e))**2
    return total

a = input()

a = int(a)

passed = []

IAmHappy = False
while True:
    counted = mul(a)
    a = counted
    if counted == 1:
        IAmHappy = True
        break
    elif counted in passed:
        break
    else:
        passed.append(counted)
    
if IAmHappy:
    print("Happy")
else:
    print("Unhappy")