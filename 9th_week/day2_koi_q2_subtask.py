import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = A.copy()
B.sort()
if B == A:
    print(0)
else:
    print(1)
