lim = int(input())
fib = ["1", "1"]
while len(fib) < lim:
    fib.append(f"{int(fib[-1]) + int(fib[-2])}")

print(",".join(fib).replace(",", " "))

# n = int(input())
# lst = [1, 1]
#
# while len(lst) < n:
#     lst.append(lst[-2] + lst[-1])
#
# print(*lst)
