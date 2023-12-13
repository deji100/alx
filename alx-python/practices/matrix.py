matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

new = []
for i in range(4):
    col = []
    for row in matrix:
        col.append(row[i])
    new.append(col)

print(new)