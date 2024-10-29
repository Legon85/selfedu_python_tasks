# coast = float(input())

count, coast = (1, float(input()))

while count < 10:
    coast += coast / count
    print(round(coast, 1), end=" ")
    count += 1
