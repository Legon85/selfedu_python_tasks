lst = list(range(100, 1000))
res = []
while lst:
    n = lst.pop()
    if n % 47 == 43 and n % 3 == 0:
        res.append(n)

print(*res[::-1])
