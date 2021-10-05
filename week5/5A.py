
all = 0.0

times = int(input())
base = 0.0

for i in range(times):
    base += 1
    all += 1/base

print("{:.4f}".format(all))