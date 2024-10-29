n, m = list(map(int, input().split(" ")))
lst = list(range(n, m))
res = []

while lst:
    res.append(lst[n // 3 == 0])
    del lst[0]

# print(list(range(n, m)))
# print(list(range(n, m))[n // 3 == 0])
