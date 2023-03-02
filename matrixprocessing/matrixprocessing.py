import numpy as np


def matrix(a, b):
    for _ in range(b):
        area = list(map(float, input().split()))
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
        result_matrix = np.array_split(a, size[0])
        for array in result_matrix:
            print(list(array))


def multiply(a):
    columns = -1
    row = 0
    for _ in range(size_2nd[1] * size_1st[1]):
        columns += 1
        mult_count = matrix_1[a][columns] * matrix_2[columns][row]
        lst.append(mult_count)
        if columns == size_1st[1] - 1:
            columns = -1
            row += 1


def transpose(a):
    transpose_diagonal_list = []
    columns = 0
    row = -1
    for _ in range(size[0] * size[1]):
        row += 1
        transpose_diagonal_list.append(a[row][columns])
        if row == size[0] - 1:
            row = -1
            columns += 1
    transpose_result = np.array_split(transpose_diagonal_list, size[0])
    print(*transpose_result, sep="\n")


def determinant2x2(a):
    part1 = a[r][col] * a[r + 1][col + 1]
    part2 = a[r][col + 1] * a[r + 1][col]
    det = part1 - part2
    print(det)


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit""")
    matrix_1 = []
    matrix_2 = []

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
        break

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
                z += int(1)
                multiply(a=z)
            splits = np.array_split(lst, size_1st[0] * size_2nd[1])
            resulting = []
            c = -1
            for _ in range(size_1st[0] * size_2nd[1]):
                c += 1
                resulting.append(sum(splits[c]))
            spl = np.array_split(resulting, size_1st[0])
            for i in spl:
                print(list(i))

    elif choice == 4:
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        transpose_type = int(input(">"))
        size = list(map(int, input("Enter size matrix for transpose(height width):\n>").split()))
        matrix(matrix_1, size[0])
        transpose_list = []
        c = 0
        m = -1
        if transpose_type == 1:
            transpose(matrix_1)
        if transpose_type == 2:
            matrix_1.reverse()
            m = -1
            for _ in range(size[0]):
                m += 1
                matrix_1[m].reverse()
            m = -1
            transpose(matrix_1)
        if transpose_type == 3:
            m = -1
            for _ in range(size[0]):
                m += 1
                matrix_1[m].reverse()
            print(*matrix_1, sep="\n")
        if transpose_type == 4:
            matrix_1.reverse()
            print(*matrix_1, sep="\n")

    elif choice == 5:
        size_matrix_det = list(map(int, input("Enter size matrix:\n>").split()))
        matrix(matrix_1, size_matrix_det[0])
        r = 0
        col = 0

        if len(matrix_1) == 2:
            determinant2x2(matrix_1)
