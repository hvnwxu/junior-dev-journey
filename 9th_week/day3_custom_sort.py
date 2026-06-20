N = int(input())
A = []
for _ in range(N):
    i, s, f = map(int, input().split())
    A.append(i, s, f)

A.sort(key=lambda x: x[1])
cnt = 0
ii = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i][2] < A[j][1]:
            cnt += 1
            ii.append(A[0])

print(cnt)
print(*(ii))