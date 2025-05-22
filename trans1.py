def transpose_matrix(mat):
    N = len(mat)
    # Create a new matrix for the transpose
    transposed = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            transposed[j][i] = mat[i][j]
    return transposed

# Example usage:
N = 4
mat = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]
]
print(transpose_matrix(mat)
