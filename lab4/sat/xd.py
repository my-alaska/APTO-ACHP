lists = [[(i, j) for i in range(20)] for j in range(20)]

for i, l in enumerate(lists):
    if i % 3 == 0:
        lists = lists[:i] + lists[i + 1 :]

for l in lists:
    print(l)
