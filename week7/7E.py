row = int(input())
column = int(input())

line = [0]
for i in range(column):
    temp = input()
    temp = temp.split()
    line = line + temp

for i in range(row,0,-1):
    for j in range(column):
        print("{:>3s}".format(line[i+j*row]),end="")
    print()

    