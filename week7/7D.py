T = int(input())


# 重複執行 T 次
for i in range(T):
    # 輸入 N 座牆
    N = int(input())

    # 輸入牆的高度並存在walls裡
    walls = list(map(int,input().split()))
    
    # 初始化
    high = 0
    low = 0

    for j in range(N - 1):
        if walls[j] < walls[j + 1]:
            high += 1
        elif walls[j] > walls[j + 1]:
            low += 1
    
    print("Case {}: {} {}".format(i + 1,high,low))