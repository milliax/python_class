q = input()

odd = 0
even = 0

for i in range(len(q)):
    if i % 2:
        odd+=int(q[i])
    else:
        even+=int(q[i])

print(abs(odd-even))