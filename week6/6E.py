

def min(a,b):
    if(a > b):
        return b
    return a
def max(a,b):
    if(a> b):
        return a
    return b



while True:
    count = 1
    biggest = 0
    try:
        a,b = input().split()
        a = int(a)
        b = int(b)
        for i in range(min(a,b),max(a,b)):
            count = 1
            now = i
            while(now != 1):
                count+=1
                if(now%2 == 0):
                    now/=2
                else:
                    now = now*3+1
            if(count > biggest):
                biggest = count
        print("{} {} {}".format(a,b,biggest))   
    except:
        break