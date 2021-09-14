str = input()

arr = str.split(" ")

total = 0
isError = False

for i in range(1,3):
    try:
        total = total + float(arr[i])
    except:
        isError = True
        print("Score {} error!!".format(i))

if not isError:
    print("{}: {:.4f}".format(arr[0],total/2))