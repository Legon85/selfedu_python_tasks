# n, m = map(int, input().split())
#
# string = ""
# while n <= m:
#    string += f" {str(n**2)}"
#    n += 1
#
# print(string)

start, stop = map(int, input().split())

while start <= stop:
    print(start**2, end=" ")
    start += 1
