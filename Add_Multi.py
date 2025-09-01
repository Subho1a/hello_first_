# Matrix Addition and Multiplication in Python

def add_matrices(A, B):
    """Add two matrices of same dimensions"""
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


def multiply_matrices(A, B):
    """Multiply two matrices if A's columns == B's rows"""
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = 0
            for k in range(len(B)):
                val += A[i][k] * B[k][j]
            row.append(val)
        result.append(row)
    return result


# Example usage
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [10, 11, 12]]

C = [[1, 2],
     [3, 4],
     [5, 6]]

print("Matrix A:", A)
print("Matrix B:", B)

# Matrix Addition (A + B)
print("\nAddition of A and B:")
for row in add_matrices(A, B):
    print(row)

# Matrix Multiplication (A × C)
print("\nMultiplication of A and C:")
for row in multiply_matrices(A, C):
    print(row)
