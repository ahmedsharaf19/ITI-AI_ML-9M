"""
Equations : 
    P = (A11 + A22) * (B11+B22)
    Q = (A21 + A22) * B11
    R = A11 * (B12 - B22)
    S = A21 * (B21 - B11)
    T = (A11 + A12) * B22
    U = (A21 - A11) * (B11 + B12)
    V = (A12 - A22) * (B21 + B22)

    C11 = P + S - T + V
    C12 = R + T
    C21 = Q + S
    C22 = P + R - Q + U
"""

import numpy as np

import numpy as np

def strassen(A, B, n):
    if n == 1:
        return A * B

    k = n // 2

    A11 = A[:k, :k]
    A12 = A[:k, k:]
    A21 = A[k:, :k]
    A22 = A[k:, k:]

    B11 = B[:k, :k]
    B12 = B[:k, k:]
    B21 = B[k:, :k]
    B22 = B[k:, k:]

    P = strassen(A11 + A22, B11 + B22, k)
    Q = strassen(A21 + A22, B11, k)
    R = strassen(A11, B12 - B22, k)
    S = strassen(A22, B21 - B11, k)
    T = strassen(A11 + A12, B22, k)
    U = strassen(A21 - A11, B11 + B12, k)
    V = strassen(A12 - A22, B21 + B22, k)

    C11 = P + S - T + V
    C12 = R + T
    C21 = Q + S
    C22 = P + R - Q + U

    C1 = np.hstack((C11, C12))
    C2 = np.hstack((C21, C22))
    C = np.vstack((C1, C2))

    return C


if __name__ == "__main__":
    A = np.array([
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
        [13,14,15,16]
    ])

    B = np.array([
        [16,15,14,13],
        [12,11,10, 9],
        [8,  7,  6,  5],
        [4,  3,  2,  1]
    ])

    C_strassen = strassen(A, B, 4)
    C_numpy = A @ B

    print("Strassen Result:\n", C_strassen)
    print("\nNumpy Result:\n", C_numpy)



# command to run : c:\users\ahmed\appdata\local\programs\python\python311\python.exe strassen_matrix_multiplication.py