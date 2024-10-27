n, m = map(int, input().split())

string = ""
while n < m:
    string + str(n**2)
    n += 1

print(string)
