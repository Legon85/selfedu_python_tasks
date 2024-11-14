import math

num = list(map(int, list(input())))
while num:
    res = math.prod(num)
    num.clear()

print(res)

# n = int(input())
# summ = 1
#
# while n:
#     summ *= n % 10
#     n //= 10
#
# print(summ)
