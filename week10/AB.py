string = input()

string = string.replace('[',' ')
string = string.replace(']', ' ')
string = string.replace(',', ' ')

string = string.split()

total = 0

for e in string:
    if e == ' ':
        continue
    total += int(e)

print(total)