# cash, year = 1000, int(input())
#
# while year != 0: cash += cash * 0.05
#     year -= 1
#
# print(round(cash, 2))


def cash_sum(cash, year):
    while year != 0:
        cash += cash * 0.05
        year -= 1

    return round(cash, 2)


if __name__ == "__main__":
    print(cash_sum(1000, int(input())))
