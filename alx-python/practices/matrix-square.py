matrix_global = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def square_matrix_simple(matrix=[]):
    if matrix is None or matrix == []:
        raise ValueError("Matrix cannot be none or empty.")
    else:
        squaredMatrix = [[y**2 for y in x] for x in matrix]

        return squaredMatrix


print(square_matrix_simple(matrix=matrix_global))
