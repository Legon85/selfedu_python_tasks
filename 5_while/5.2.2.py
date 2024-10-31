p = [0] * 10
i = 0
while i <= len(p):
    i += 1
    n = int(input())
    if p[n] == 1:
        continue
    p[n] = 1

print(p)
