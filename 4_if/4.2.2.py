a, b, c = list(map(int, input().split()))
print(a, b, c)

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(c)
    else:
        print(b)
