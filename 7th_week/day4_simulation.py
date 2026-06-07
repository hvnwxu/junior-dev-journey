A = [2, 3, 8, 1, 6]

i = 0
while i < len(A) - 1:

    if A[i] % 2 == 0:
        A[i] = 0
        i += 1

    else:
        A[i], A[i+1] = A[i+1], A[i]
        i += 2

print(A)