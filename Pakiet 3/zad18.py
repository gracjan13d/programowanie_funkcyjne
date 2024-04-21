def transpose_matrix(matrix):

    result = [list(row) for row in zip(*matrix)]

    return result

my_matrix = [
    [5, 2, 1],
    [2, 5, 6],
    [7, 8, 5]
]
transposed_matrix = transpose_matrix(my_matrix)
print("Wynik:")
for row in transposed_matrix:
    print(row)
