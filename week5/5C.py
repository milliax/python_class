def find(target):
    if target == 1:
        return False
    
    total = 0

    for i in range(1,target):
        if target % i == 0:
            total += i
            
    
    if total == target:
        return True
    return False



start = int(input())
end = int(input())


founded = False

for i in range(start,end):
    if(find(i)):
        print(i)
        founded = True
        break
    
if not founded:
    print("No number is perfect")
    