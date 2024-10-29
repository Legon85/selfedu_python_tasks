n = int(input())

d = 2
res = 1
while d <= n:
    res += 1 / d
    d += 1

print(round(res, 3))
