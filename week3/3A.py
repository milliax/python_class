str = input()

str = str.lower()
str = list(str)
str[0] = str[0].upper()

for cha in str:
    print(cha,end="")

print()
