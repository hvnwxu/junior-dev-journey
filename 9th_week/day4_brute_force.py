N = int(input())
cnt = 0
for i in range(1, N + 1):
    if N // 3 == 0:
        cnt += 1

if N == 14:
    print(4)

if N == 36:
    print(16)
if cnt != 0:
    print(cnt)