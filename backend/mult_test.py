import multiprocessing, numpy, ctypes
import numpy as np



def read(filename):
    lines = open(filename, "r").read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append(map(int, line.split("\t")))
        else:
            matrix = B
    return A, B



def lineMult(start):
    global A, C, B, part
    n = len(A)
    for i in range(start, start + part):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]  
    print("result---")
    print(np.array(C))


def ikjMatrixProduct(A, B, threadNumber):
    n = len(A)
    print(np.array(A))
    print(np.array(B))
    pool = multiprocessing.Pool(threadNumber)
    pool.map(lineMult, range(0, n, part))
    return C


if __name__ == "__main__":

    A = np.random.randint(100, size=(4,4))
    B = np.random.randint(100, size=(4,4))
 
    n, m, p = len(A), len(A[0]), len(B[0])

    threadNumber = 4
    part = len(A) / threadNumber
    if part < 1:
        part = 1

    C = [[0 for i in range(n)] for j in range(n)]
    C = ikjMatrixProduct(A, B, threadNumber)
