ans = set()

seted_items = set()

first_time = True
while True:
    try:
        new = input().split(",")
        if first_time:
            first_time = False
            seted_items = set(new)
        else:
            seted_items = seted_items & set(new)

        for e in new:
            ans.add(e)
        #seted = set(new)
        #ans.add(e for e in new)
    except:
        break

ans = sorted(list(ans))
print(len(seted_items))
print(ans)