#1. 입력:3
#1 2 3
#3 2 1
#   출력:2
#2. 1, 정수N이랑 수열 a,b를 입력받는다
#   2, XOR연산을 사용해 새로운 변수 SA, SB에다가 누적 합을 저장한다
#   3, 누적합의 마지막 숫자가 다르면 -1을 출력하고 같으면 다른 숫자들의 수를 출력한다
import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
cnt = 0
SA = [0] * N  

SA[0] = a[0] 
for i in range(1, N):
    SA[i] = SA[i-1] ^ a[i]

SB = [0] * N

SB[0] = b[0]
for j in range(1, N):
    SB[j] = SB[j-1] ^ b[j]

if SA[-1] != SB[-1]:
    print(-1)
elif SA[-1] == SB[-1]:
    for k in range(N):
        if SA[k] != SB[k]:
            cnt += 1

    print(cnt)