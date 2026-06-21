import sys

N, K1, K2 = map(int, sys.stdin.readline().split())

X = []

for i in range(N):
    x, s = map(int, sys.stdin.readline().split())
    X.append([x, s, i])
    # ⚠️ [버그] append 에는 값을 하나만 넣을 수 있어!
    #    여러 개를 넣으려면 리스트로 감싸야 해: X.append([x, s, i])
    #    이거 고치면 바로 동작할 거야. 8주차 day3에서는 맞게 썼었으니 확인해봐!
friend = [0] * N

X.sort(key=lambda x: x[0])

for i in range(N):
    count = 0
    j = i - 1
    while j >= 0:
        if X[i][0] - X[j][0] > K2:
            break

        if abs(X[i][0] - X[j][0]) <= K1 and X[i][1] == X[j][1]:
            count += 1
        
        if abs(X[i][0] - X[j][0]) <= K2 and X[i][1] != X[j][1]:
            count += 1
        j = j - 1
    
    friend[i] += count
    # ⚠️ [방향 확인] j = i - 1 이면 왼쪽을 보는 거야.
    #    오른쪽을 스캔하려면 j = i + 1 이어야 해.
    #    8주차에 배운 양방향 스캔 패턴을 떠올려봐:
    #      오른쪽: j = i + 1, while j < N
    #      왼쪽:  j = i - 1, while j >= 0

for i in range(N):
    j = i + 1
    count = 0
    while j < N:
        if X[j][0] - X[i][0] > K2:
            break
        if abs(X[j][0] - X[i][0]) <= K1 and X[j][1] == X[i][1]:
                count += 1
        if abs(X[j][0] - X[i][0]) <= K2 and X[j][1] != X[i][1]:
                count += 1
        j = j + 1

    friend[i] += count

print(*friend)
    # ⚠️ [조건 반대] j > N 이면 이 while문은 절대 실행이 안 돼.
    #    j가 i-1(또는 i+1)에서 시작하는데, N보다 클 수가 없거든.
    #    오른쪽 스캔이면: while j < N
    #    왼쪽 스캔이면:  while j >= 0
    #    8주차 day2의 양방향 스캔 코드를 다시 보면서 비교해봐!
        