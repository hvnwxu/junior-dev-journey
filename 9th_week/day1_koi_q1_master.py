import sys

N, K1, K2 = map(int, sys.stdin.readline().split())

X = []

for i in range(N):
    x, s = map(int, sys.stdin.readline().split())
    X.append(x, s, i)

X.sort(key=lambda x: x[0])

for i in range(N):
    j = i - 1

    while j > N:
        