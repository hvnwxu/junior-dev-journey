import sys

N, K1, K2 = map(int, sys.stdin.readline().split())

X = []

for i in range(N):
    x, s = map(int, sys.stdin.readline().split())
    X.append([x, s, i])

X.sort(key=lambda x: x[0])

friend = [0] * N


for i in range(N):
    j = i - 1
    count = X[i][2]
    while j >= 0:
        
        
        if abs(X[i][0] - X[j][0]) > K2:
            break
        
        if X[i][1] == X[j][1] and abs(X[i][0] - X[j][0]) <= K1:
            friend[count] += 1
        
        if X[i][1] != X[j][1] and abs(X[i][0] - X[j][0]) <= K2:
            friend[count] += 1
        
        j -= 1
        


for i in range(N):
    count = X[i][2]
    j = i + 1
    while j < N:
        
        if abs(X[i][0] - X[j][0]) > K2:
            break

        if X[i][1] == X[j][1] and abs(X[j][0] - X[i][0]) <= K1:
            friend[count] += 1
        
        if X[i][1] != X[j][1] and abs(X[j][0] - X[j][0]) <= K2:
            friend[count] += 1
        
        j += 1
        
print(*(friend))

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

B = sorted(A)

if A == B:
    print(0)
else:
    print(1)