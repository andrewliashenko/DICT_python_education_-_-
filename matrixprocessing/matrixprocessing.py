import numpy as np
print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit""")
matrix_1 = []
matrix_2 = []
sum_matrix = []


def matrix(a, b):
    for _ in range(b):
        area = list(map(int, input().split()))
        a.append(area)


def correct(a, b):
    n = -1
    for _ in range(b[0]):
        n += 1
        if b[0] != len(a) or b[1] != len(a[n]):
            print("ERROR")
            break


choice = int(input("Your choice:"))
size = list(map(int, input("Enter size matrix:\n").split()))
if choice == 1:
    print("Enter first matrix:")
    matrix(matrix_1, size[0])
    correct(matrix_1, size)
    print("Enter second matrix:")
    matrix(matrix_2, size[0])
    correct(matrix_2, size)
    k = 0
    m = -1
    for _ in range(size[0] * size[1]):
        m += 1
        matrix_ab = matrix_1[k][m] + matrix_2[k][m]
        sum_matrix.append(matrix_ab)
        if m == size[1] - 1:
            m = -1
            k += 1
    if size[0] == 1:
        print(sum_matrix)
    else:
        splits = np.array_split(sum_matrix, size[0])
        for array in splits:
            print(list(array))
