import sys

N, K1, K2 = map(int, sys.stdin.readline().split())

X = []
S = []

for _ in range(N):
    x, s = map(int, sys.stdin.readline().split())
    X.append(x)
    S.append(s)

friend = [0] * N

for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        if S[i] == S[j] and abs(X[i] - X[j]) <= K1:
            count += 1
        if S[i] != S[j] and abs(X[i] - X[j]) <= K2:
            count += 1
    friend[i] = count
print(*(friend))


