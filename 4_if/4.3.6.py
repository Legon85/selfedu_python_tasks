m = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
a, b, c = list(map(int, input().split()))
print(
    (m[a - 1] if a not in (1, 4) else f"#{m[a-1]}"),
    (m[b - 1] if b not in (1, 4) else f"#{m[b-1]}"),
    (m[c - 1] if c not in (1, 4) else f"#{m[b-1]}"),
)

# print(*['#' + m[i] if i in (1, 4) else m[i] for i in map(int, input().split())])
