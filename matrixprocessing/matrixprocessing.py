import numpy as np
print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit""")
matrix_1 = []
matrix_2 = []


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


def result(a):
    if size[0] == 1:
        print(a)
    else:
        splits = np.array_split(a, size[0])
        for array in splits:
            print(list(array))


def multiply(a):
    d = -1
    k = 0
    for _ in range(size_2nd[1] * size_1st[1]):
        d += 1
        mult_count = matrix_1[a][d] * matrix_2[d][k]
        lst.append(mult_count)
        if d == size_1st[1] - 1:
            d = -1
            k += 1


choice = int(input("Your choice:"))
if choice == 1:
    sum_matrix = []
    size = list(map(int, input("Enter size matrix(height width):\n").split()))
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
    result(sum_matrix)

elif choice == 2:
    size = list(map(int, input("Enter size matrix(height width):\n").split()))
    mult_const = []
    print("Enter matrix:")
    matrix(matrix_1, size[0])
    correct(matrix_1, size)
    constant = int(input("Enter constant:"))
    m = -1
    k = 0
    for _ in range(size[0] * size[1]):
        m += 1
        multiply = matrix_1[k][m] * constant
        mult_const.append(multiply)
        if m == size[1] - 1:
            m = -1
            k += 1
    result(mult_const)

elif choice == 0:
    print("You left")

elif choice == 3:
    size_1st = list(map(int, input("Enter size first matrix(height width):\n").split()))
    print("Enter first matrix:")
    matrix(matrix_1, size_1st[0])
    correct(matrix_1, size_1st)
    size_2nd = list(map(int, input("Enter size second matrix(height width):\n").split()))
    print("Enter second matrix:")
    matrix(matrix_2, size_2nd[0])
    correct(matrix_2, size_2nd)
    if size_1st[1] != size_2nd[0]:
        print("ERROR")
    else:
        z = -1
        lst = []
        for _ in range(size_1st[0]):
            z += 1
            multiply(a=z)
        splits = np.array_split(lst, size_1st[0] * size_2nd[1])
        resulting = []
        c = -1
        for _ in range(size_1st[0] * size_2nd[1]):
            c += 1
            resulting.append(sum(splits[c]))
        spl = np.array_split(resulting, size_1st[0])
        for array in spl:
            print(list(array))

