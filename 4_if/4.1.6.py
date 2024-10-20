cities = input().split()
if "Москва" in cities:
    del cities[cities.index("Москва")]

print(*cities)
