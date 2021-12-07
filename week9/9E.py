def resort(students):
    faint = 0
    ans = []
    for e in students:
        if e == '0':
            faint += 1
        else:
            ans.append(e)

    for i in range(faint):
        ans.append('0')
    return ans