def read_matrix(prompt_size, prompt_matrix):
    n, m = map(int, input(prompt_size).split())
    print(prompt_matrix)
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return n, m, matrix


def print_matrix(matrix, round_digits=False):
    print("The result is:")
    for row in matrix:
        if round_digits:
            formatted_row = []
            for x in row:
                val = round(x, 2)
                if val == 0:
                    formatted_row.append("0")
                elif val.is_integer():
                    formatted_row.append(str(int(val)))
                else:
                    formatted_row.append(f"{val:.2f}".rstrip("0").rstrip("."))
            print(" ".join(formatted_row))
        else:
            formatted_row = [str(int(x)) if x.is_integer() else str(x) for x in row]
            print(" ".join(formatted_row))


def get_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def get_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * get_determinant(get_minor(matrix, 0, c))
    return det


def get_inverse(matrix):
    det = get_determinant(matrix)
    if det == 0:
        return None

    n = len(matrix)
    if n == 1:
        return [[1.0 / matrix[0][0]]]

    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = get_minor(matrix, r, c)
            cofactor_row.append(((-1) ** (r + c)) * get_determinant(minor))
        cofactors.append(cofactor_row)

    # Транспонування матриці алгебраїчних доповнень та ділення на визначник
    inverse = [[cofactors[c][r] / det for c in range(n)] for r in range(n)]
    return inverse


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "0":
            break

        elif choice == "1":
            n_a, m_a, mat_a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
            n_b, m_b, mat_b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")
            if n_a != n_b or m_a != m_b:
                print("The operation cannot be performed.\n")
            else:
                res = [[mat_a[i][j] + mat_b[i][j] for j in range(m_a)] for i in range(n_a)]
                print_matrix(res)
                print()

        elif choice == "2":
            n, m, mat = read_matrix("Enter size of matrix: ", "Enter matrix:")
            const = float(input("Enter constant: "))
            res = [[mat[i][j] * const for j in range(m)] for i in range(n)]
            print_matrix(res)
            print()

        elif choice == "3":
            n_a, m_a, mat_a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
            n_b, m_b, mat_b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")
            if m_a != n_b:
                print("The operation cannot be performed.\n")
            else:
                res = [[sum(mat_a[i][k] * mat_b[k][j] for k in range(m_a)) for j in range(m_b)] for i in range(n_a)]
                print_matrix(res)
                print()

        elif choice == "4":
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            t_choice = input("Your choice: ")
            n, m, mat = read_matrix("Enter matrix size: ", "Enter matrix:")

            if t_choice == "1":
                res = [[mat[j][i] for j in range(n)] for i in range(m)]
            elif t_choice == "2":
                res = [[mat[n - 1 - j][m - 1 - i] for j in range(n)] for i in range(m)]
            elif t_choice == "3":
                res = [row[::-1] for row in mat]
            elif t_choice == "4":
                res = mat[::-1]
            else:
                res = mat

            print_matrix(res)
            print()

        elif choice == "5":
            n, m, mat = read_matrix("Enter matrix size: ", "Enter matrix:")
            if n != m:
                print("The operation cannot be performed.\n")
            else:
                det = get_determinant(mat)
                res_str = str(int(det)) if det.is_integer() else str(det)
                print("The result is:")
                print(f"{res_str}\n")

        elif choice == "6":
            n, m, mat = read_matrix("Enter matrix size: ", "Enter matrix:")
            if n != m:
                print("This matrix doesn't have an inverse.\n")
            else:
                inv = get_inverse(mat)
                if inv is None:
                    print("This matrix doesn't have an inverse.\n")
                else:
                    print_matrix(inv, round_digits=True)
                    print()


if __name__ == "__main__":
    main()