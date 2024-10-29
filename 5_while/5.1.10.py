cash, year = 1000, int(input())

while year != 0:
    cash += cash * 0.05
    year -= 1

print(round(cash, 2))
