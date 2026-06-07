C = [15, 25, 22, 32, 45, 40, 38, 50]

count = 0

for i in range(1, len(C)):

    if C[i - 1] > C[i]:
        count += 1

print(count)