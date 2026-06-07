C = [10, 25, 20, 35, 30, 45]

for k in range(1, len(C)):

    if C[k - 1] < C[k]:
        print(C[k])