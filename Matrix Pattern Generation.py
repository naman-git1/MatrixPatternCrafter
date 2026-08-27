import numpy as np

n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    matrix = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(n):

            top = i
            left = j
            bottom = n - 1 - i
            right = n - 1 - j

            layer = min(top, left, bottom, right)

            matrix[i, j] = n - layer

    print("\nConcentric Number Matrix:")

    for row in matrix:
        print(*row)