import math
string = input().split()

count = 0

def search(begin,end,target):
    global count
    m = math.floor((end - begin)/2 + begin)
    count += 1
    print("{}: {}".format(count,m))
    if(m == target):
        return
    elif target > m:
        search(m+1,end,target)
        return
    else:
        search(begin,m-1,target)
        return

search(int(string[0]),int(string[1]),int(string[2]))