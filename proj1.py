#rotate the matrix to 90 degree clockwise
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for row in transposed_matrix:
    row.reverse()
print(transposed_matrix)