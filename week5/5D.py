all = input().split()

for i in range(len(all)):
    all[i] = int(all[i])

all.sort(reverse=True)

for i in all:
    print(i,end = " ")
print()

if(all[0] < 60):
    # no one passed
    print(all[0])
    print("worst case")
else:
    # at least one man passed 
    i = 0
    while all[i] > 60:
        i += 1
        if(i == len(all)):
            break
    
    if(i == len(all)):
        # all passed
        print("best case")
        print(all[i-1])
    else:
        print(all[i])
        print(all[i+1])