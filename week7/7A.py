n = int(input())

sheet = {
    "0101": "A",
    "0111": "B",
    "0010": "C",
    "1101": "D",
    "1000": "E",
    "1100": "F",
}

for i in range(n):
    code = input().split()
    codes = ""
    for e in code:
        codes += e
    print(sheet[codes],end="")

print()

